#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
