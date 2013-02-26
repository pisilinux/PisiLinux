#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="CharisSILCompact"

def install():
    shelltools.chmod("*.ttf",0644)
    shelltools.chmod("*.txt",0644)

    pisitools.insinto("/usr/share/fonts/charis","*.ttf")

    pisitools.dosym("../conf.avail/sil-charis-compact-fonts-fontconfig.conf", "/etc/fonts/conf.d/sil-charis-compact-fonts-fontconfig.conf")

    pisitools.dodoc("*.txt")
