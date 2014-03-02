#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/share/fonts/oxygen", "*/*.ttf")

    pisitools.dodoc("COPYING-OFL", "README")
