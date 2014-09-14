#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4

def setup():
    shelltools.system("lrelease boncuk.pro")
    qt4.configure("boncuk.pro")

def build():
    qt4.make()

def install():
    pisitools.dobin("bin/boncuk")
    pisitools.insinto("/usr/share/pixmaps", "resources/boncuk.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO", "NEWS")
