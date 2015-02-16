#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
                         --enable-netcdf-4 \
                         --enable-dap-netcdf \
                         --disable-static \
                        ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")    

def build():
    autotools.make()

def check():
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("README")
