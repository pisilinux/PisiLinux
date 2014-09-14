#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    pisitools.dosed("h/pchs.h", "qtermwidget/qtermwidget.h", "qtermwidget4/qtermwidget.h")
    pisitools.dosed("cpp/mainwindow.cpp", "qtermwidget/qtermwidget.h", "qtermwidget4/qtermwidget.h")
    qt4.configure()

def build():
    pisitools.dosed("Makefile", "-lqtermwidget", "-lqtermwidget4")
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("LICENSE", "LISANS", "OKUBUNU", "README")
