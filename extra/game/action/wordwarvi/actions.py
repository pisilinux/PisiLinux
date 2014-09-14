#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("Makefile", "OPTIMIZE_FLAG=-O3", "OPTIMIZE_FLAG=%s" % get.CFLAGS())

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    for icon in shelltools.ls("icons/*.png"):
        dimensions = icon[icon.rfind("_") + 1:-4]
        pisitools.insinto("/usr/share/icons/hicolor/%s/apps/" % dimensions, icon, "wordwarvi.png")

    pisitools.dodoc("COPYING", "AUTHORS", "changelog.txt", "README", "AAA_HOW_TO_MAKE_NEW_LEVELS.txt")
