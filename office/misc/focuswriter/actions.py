#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.insinto("/usr/share/pixmaps/",
            "resources/images/icons/hicolor/32x32/apps/focuswriter.png")
    pisitools.dodoc("ChangeLog", "COPYING", "README*")
