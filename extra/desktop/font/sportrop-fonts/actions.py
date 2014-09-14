#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="."

def install():
    shelltools.chmod("*.ttf", 0644)
    pisitools.insinto("/usr/share/fonts/sportrop/","*.ttf")
