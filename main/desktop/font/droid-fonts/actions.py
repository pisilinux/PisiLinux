#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "droid-%s" % get.srcVERSION().split("_", 1)[1]
WorkDir = "base"

def install():
    shelltools.chmod("*.ttf",0644)

    pisitools.insinto("/usr/share/fonts/droid","*.ttf")

    pisitools.dosym("../conf.avail/65-droid-fonts-sans-fontconfig.conf", "/etc/fonts/conf.d/65-droid-fonts-sans-fontconfig.conf")
    pisitools.dosym("../conf.avail/60-droid-fonts-sans-mono-fontconfig.conf", "/etc/fonts/conf.d/60-droid-fonts-sans-mono-fontconfig.conf")
    pisitools.dosym("../conf.avail/59-droid-fonts-serif-fontconfig.conf", "/etc/fonts/conf.d/59-droid-fonts-serif-fontconfig.conf")

    pisitools.dodoc("NOTICE", "README.txt")
