#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="CharisSIL-4.112"

def install():
    shelltools.chmod("*.ttf",0644)
    shelltools.chmod("*.txt",0644)

    pisitools.insinto("/usr/share/fonts/charis","*.ttf")

    pisitools.dosym("../conf.avail/sil-charis-compact-fonts-fontconfig.conf", "/etc/fonts/conf.d/sil-charis-compact-fonts-fontconfig.conf")

    pisitools.dodoc("*.txt")
