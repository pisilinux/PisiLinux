#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("pokerth.desktop", "Categories=Qt;Game;CardGame;", "Categories=Game;CardGame;")
    shelltools.system("qmake pokerth.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("pokerth")
    pisitools.dobin("bin/*")

    pisitools.insinto("/usr/share/pokerth","data")
    pisitools.insinto("/usr/share/pixmaps","pokerth.png")
    pisitools.insinto("/usr/share/applications", "pokerth.desktop")

    # Remove bundled fonts
    #pisitools.remove("/usr/share/pokerth/data/fonts/VeraBd.ttf")
    #pisitools.remove("/usr/share/pokerth/data/fonts/c059013l.pfb")
    #pisitools.remove("/usr/share/pokerth/data/fonts/n019003l.pfb")

    # and replace them with symlinks
    shelltools.sym("/usr/share/fonts/Type1/c059013l.pfb", "%s/usr/share/pokerth/data/fonts/c059013l.pfb" % get.installDIR())
    shelltools.sym("/usr/share/fonts/Type1/n019003l.pfb", "%s/usr/share/pokerth/data/fonts/n019003l.pfb" % get.installDIR())
    shelltools.sym("/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf", "%s/usr/share/pokerth/data/fonts/VeraBd.ttf" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "TODO")