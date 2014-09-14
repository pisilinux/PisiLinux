#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/icons", "Pacifica")

    pisitools.dosym("/usr/share/icons/Pacifica/16x16/apps/xchat.png", "/usr/share/icons/Pacifica/16x16/apps/cancel.png")
    pisitools.dosym("/usr/share/icons/Pacifica/22x22/apps/xchat.png", "/usr/share/icons/Pacifica/22x22/apps/cancel.png")
    pisitools.dosym("/usr/share/icons/Pacifica/32x32/apps/xchat.png", "/usr/share/icons/Pacifica/32x32/apps/cancel.png")
    pisitools.dosym("/usr/share/icons/Pacifica/48x48/apps/xchat.png", "/usr/share/icons/Pacifica/48x48/apps/cancel.png")

    pisitools.dodoc("CREDITS", "README.md")
