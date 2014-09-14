#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="Gentium102"

def install():
    shelltools.chmod("*.TTF",0644)
    shelltools.chmod("*.txt",0644)

    pisitools.insinto("/usr/share/fonts/gentium/","*.TTF")

    pisitools.dodoc("GENTIUM-FAQ.txt","OFL-FAQ.txt","OFL.txt","QUOTES.txt","FONTLOG.txt")
