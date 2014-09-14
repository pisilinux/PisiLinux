#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("LC_ALL", "C")

def setup():

    autotools.autoreconf("-fi")
    # All the other directories are configured through prefix.
    # autotools.configure() overrides them causing some directories
    # not prefixed by /var/pisi while installing, boom sandbox violations.
    # Briefly, use rawConfigure() here, (Fixes #8738)
    autotools.rawConfigure('--prefix=/usr \
                            --build=%s \
                            --disable-static \
                            --with-f77=gfortran \
                            --with-lapack \
                            --with-blas \
                            --with-glpk \
                            --with-opengl \
                            --disable-java \
                            --with-umfpack="-lumfpack -lsuitesparseconfig" \
                            --enable-shared' % get.HOST())

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1") #use parallel build patch to turn parallel build on

def install():
    autotools.install()

    # Clean /var/pisi references
    for header in ["defaults.h", "oct-conf.h"]:
        pisitools.dosed("%s/usr/include/octave-%s/octave/%s" % (get.installDIR(), get.srcVERSION(), header), "%s" % get.installDIR(), "")

    # Set LDPATH for octave
    pisitools.dodir("/etc/ld.so.conf.d")
    shelltools.echo("%s/etc/ld.so.conf.d/99-octave.conf" % get.installDIR(), "/usr/lib/octave-%s" % get.srcVERSION())

