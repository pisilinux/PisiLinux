#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
	#pisitools.dosed("src/CMakeLists.txt", "KDE_KDEUI_LIBS}", "KDE_KDEUI_LIBS} -lkdeui -lQtGui -lkdecore -lQtCore ")
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("LICENSE", "README")

