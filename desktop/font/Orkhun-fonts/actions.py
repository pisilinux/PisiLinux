#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "orkhun"

def install():
    shelltools.chmod("*.ttf", 0644)
    pisitools.insinto("/usr/share/fonts/orkhun/", "*.ttf")

    pisitools.dodoc("LICENSE", "README")

