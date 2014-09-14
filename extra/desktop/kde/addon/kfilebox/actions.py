#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

    pisitools.dosed("Makefile", "-I/usr/include/QtDBus", "-I/usr/include/QtDBus -I/usr/include/kde4")

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dodoc("README")
