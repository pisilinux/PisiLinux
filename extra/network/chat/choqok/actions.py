#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dosym("/usr/share/icons/hicolor/128x128/apps/choqok.png", "/usr/share/pixmaps/choqok.png")

    # Dont pollute Actions menu with useless service menus
    pisitools.remove("/usr/share/kde4/services/ServiceMenus/choqok_share.desktop")
    pisitools.remove("/usr/share/kde4/services/ServiceMenus/choqok_upload.desktop")

    pisitools.dodoc("AUTHORS", "changelog", "COPYING", "README", "TODO")
