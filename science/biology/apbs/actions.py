#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    for d in ("zlib", "opal", "blas"):
        shelltools.unlinkDir("contrib/%s" % d)

    shelltools.unlink("acinclude.m4")

    pisitools.dosed("Makefile.am", "GENTOO_PKG_NAME", get.srcNAME())
    pisitools.dosed("examples/Makefile.am", "ion-pmf")

    libtools.libtoolize()
    autotools.autoreconf()
    autotools.configure("--enable-python \
                         --disable-zlib \
                         --enable-tools \
                         --disable-static \
                         --enable-shared \
                         --with-blas='-lf77blas -latlas -lblas' \
                         FFLAGS='%s -I/usr/include/atlas' \
                         CFLAGS='%s -DVF77_ONEUNDERSCORE'" % (get.CFLAGS(), get.CFLAGS()))


def build():
    autotools.make()

def check():
    # Be careful, requires long looong time...
    shelltools.export("LC_NUMERIC", "C")
    shelltools.cd("examples")
    autotools.make("test")

def install():

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/var")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

    #Needed by APBS plugin of PyMOL
    shelltools.chmod("tools/manip/psize.py", 0755)
    pisitools.insinto("/usr/bin", "tools/manip/psize.py", "psize")

    #create freemol directory and symlink, some programs (like pymol) may look here to source python file directly
    pydir = "/usr/lib/%s/site-packages/" % get.curPYTHON()
    pisitools.dodir("%s/pymol/freemol/bin" % pydir)
    pisitools.dosym("/usr/bin/psize", "%s/pymol/freemol/bin/psize.py" % pydir)
