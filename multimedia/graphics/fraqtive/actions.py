#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dosed("src/fraqtive.desktop", "Categories=Qt;Education;Science;Math;", "Categories=Qt;Graphics;")
    qt4.install()
