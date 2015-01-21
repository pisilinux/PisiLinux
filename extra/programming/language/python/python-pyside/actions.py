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
    shelltools.cd("./pyside-qt4.8+1.2.2")
    shelltools.makedirs("build2")
    #shelltools.makedirs("build3")
    shelltools.cd("build2")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DBUILD_TESTS=OFF \
                          -DPYTHON_SUFFIX=-python2.7", sourceDir="..")
    #python3
    #shelltools.cd("../build3")
    #cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          #-DCMAKE_BUILD_TYPE=Release \
                          #-DBUILD_TESTS=OFF", sourceDir="..")
def build():
    #python2
    shelltools.cd("pyside-qt4.8+1.2.2/build2")
    autotools.make()
    #python3
    #shelltools.cd("../build3")
    #autotools.make()

def install():
    #Python2
    shelltools.cd("pyside-qt4.8+1.2.2/build2")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.rename("/usr/lib/pkgconfig/pyside.pc", "pyside-py2.pc")

    #Python3
    #shelltools.cd("../build3")
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.rename("/usr/lib/pkgconfig/pyside.pc", "pyside-py3.pc")
