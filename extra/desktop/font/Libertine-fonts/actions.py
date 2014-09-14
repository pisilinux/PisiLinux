#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "LinLibertineSRC"
shelltools.export("HOME", get.workDIR())

def build():
    shelltools.system("fontforge -lang=ff -script buildscript *.sfd")

def install():
    pisitools.insinto("/usr/share/fonts/libertine","*.ttf")

    pisitools.dodoc("*.txt")
