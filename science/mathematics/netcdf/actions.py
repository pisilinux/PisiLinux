#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CPPFLAGS", "-DNDEBUG -fPIC")
    shelltools.export("FC", "gfortran")
    shelltools.export("F90", "gfortran")
    shelltools.export("FFLAGS", "-fPIC %s" % get.CFLAGS())
    shelltools.export("FCFLAGS", "-fPIC %s" % get.CFLAGS())
    shelltools.export("F90FLAGS", "-fPIC %s" % get.CFLAGS())

    autotools.configure("--enable-shared \
                         --disable-static")

def build():
    autotools.make("-j1")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/include/netcdf")
    pisitools.domove("/usr/include/*.*", "/usr/include/netcdf")

    pisitools.dodoc("README", "RELEASE_NOTES")
