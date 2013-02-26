#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
