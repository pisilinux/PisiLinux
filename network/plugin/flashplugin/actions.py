# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

ARCH = "i386" if get.ARCH() == "i686" else "x86_64"
WorkDir = get.ARCH()
NoStrip = "/"

def install():
    pisitools.insinto("/usr/bin/", "usr/bin/flash-player-properties")
    pisitools.insinto("/usr/lib/kde4/", "usr/lib/kde4/kcm_adobe_flash_player.so")
    pisitools.insinto("/usr/", "usr/share/")

    if get.ARCH() == "x86_64":
        pisitools.insinto("/usr/lib/kde4", "usr/lib64/kde4/kcm_adobe_flash_player.so")

    pisitools.doexe("libflashplayer.so", "/usr/lib/browser-plugins")