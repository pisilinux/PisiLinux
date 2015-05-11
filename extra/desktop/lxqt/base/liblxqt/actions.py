#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DLXQT_ETC_XDG_DIR==/usr/share/cmake/qt5xdg \
                          -DKF5WindowSystem_DIR=/usr/lib/cmake/KF5WindowSystem \
                          -DLXQT_LIBRARY_DIRS=lib", sourceDir="..")
def build():
    shelltools.cd("build")
    cmaketools.make()
    pisitools.dosed("CMakeFiles/Export/_usr/share/cmake/lxqt/lxqt-targets-release.cmake", "/usr/lib64/liblxqt.so.0.9.0", "/usr/lib/liblxqt.so.0.9.0")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/lib64/*", "usr/lib/")
    pisitools.removeDir("/usr/lib64")
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING")
