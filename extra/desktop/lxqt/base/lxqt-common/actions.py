#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/etc/lxqt/*.conf")
    pisitools.remove("etc/pcmanfm-qt/lxqt/*.conf")

    pisitools.remove("/usr/share/lxqt/themes/a-mego/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/ambiance/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/flat/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/flat-dark-alpha/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/green/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/light/mainmenu.svg")
    pisitools.remove("/usr/share/lxqt/themes/plasma-next-alpha/mainmenu.svg")   
    pisitools.remove("/usr/share/lxqt/themes/a-mego/*.jpg")
    pisitools.remove("/usr/share/lxqt/themes/ambiance/*.jpg")
    pisitools.remove("/usr/share/lxqt/themes/flat-dark-alpha/*.jpg")
    pisitools.remove("/usr/share/lxqt/themes/a-mego/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/ambiance/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/flat/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/flat-dark-alpha/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/green/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/light/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/plasma-next-alpha/wallpaper.cfg")
    pisitools.remove("/usr/share/lxqt/themes/flat/*.png")

    pisitools.dodoc("README.md")