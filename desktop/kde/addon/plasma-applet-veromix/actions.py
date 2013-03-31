#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/kde4/apps/plasma/plasmoids/veromix-plasmoid/contents", "contents/*")
    pisitools.insinto("/usr/share/kde4/apps/plasma/plasmoids/veromix-plasmoid/dbus-service", "dbus-service/*")
    pisitools.insinto("/usr/share/kde4/apps/plasma/plasmoids/veromix-plasmoid", "metadata.desktop")
    pisitools.insinto("/usr/share/kde4/services", "metadata.desktop", "plasma-applet-veromix-plasmoid.desktop")
