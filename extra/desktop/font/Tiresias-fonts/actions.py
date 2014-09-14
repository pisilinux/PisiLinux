#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="tiresias"

def install():
        shelltools.chmod("*.ttf",0644)

        pisitools.insinto("/usr/share/fonts/tiresias/", "*.ttf")
        pisitools.insinto("/usr/share/fonts/tiresias/", "*.TTF")

        pisitools.dosym("../conf.avail/tiresias-fonts-info-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-info-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-info-z-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-info-z-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-key-v2-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-key-v2-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-lp-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-lp-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-pc-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-pc-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-pc-z-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-pc-z-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-sign-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-sign-fontconfig.conf")
        pisitools.dosym("../conf.avail/tiresias-fonts-sign-z-fontconfig.conf", "/etc/fonts/conf.d/tiresias-fonts-sign-z-fontconfig.conf")

        pisitools.dodoc("COPYING/*.doc", "COPYING/*.txt")
