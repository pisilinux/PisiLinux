# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

WorkDir = "."

def setup():
    #python2
    shelltools.cd("shiboken-1.2.2/")
    shelltools.makedirs("build2")
    #shelltools.makedirs("build3")
    shelltools.cd("build2")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                          -DCMAKE_INSTALL_SYSCONFDIR=/etc \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")

    #python3
    #shelltools.cd("../build3")
    #cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
                          #-DCMAKE_INSTALL_SYSCONFDIR=/etc \
                          #-DUSE_PYTHON3=yes \
                          #-DBUILD_TESTS=OFF \
                          #-DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir="..")

def build():
    #python2
    shelltools.cd("shiboken-1.2.2/build2")
    autotools.make()
    #python3
    #shelltools.cd("../build3")
    #autotools.make()
def install():
    #Python2
    shelltools.cd("shiboken-1.2.2/build2")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.rename("usr/lib/pkgconfig/shiboken.pc", "shiboken-py2.pc")
    #pisitools.remove("usr/lib/cmake/Shiboken-1.2.2/ShibokenConfigVersion.cmake")
    #pisitools.remove("usr/lib/cmake/Shiboken-1.2.2/ShibokenConfig.cmake")
    #Python3
    #shelltools.cd("../build3")
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.rename("usr/lib/pkgconfig/shiboken.pc", "shiboken-py3.pc")
    #pisitools.removeDir("usr/bin")
    #pisitools.removeDir("usr/include")
    #pisitools.removeDir("usr/share")

