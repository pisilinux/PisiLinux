#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("plasma-applet-translatoid.desktop", "Name=Translator", "Name=Translatoid")
    pisitools.dosed("plasma-applet-translatoid.desktop", "Icon=translator.png", "Icon=accessories-dictionary.png")

    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    pisitools.dodoc("licence.txt", "README")
