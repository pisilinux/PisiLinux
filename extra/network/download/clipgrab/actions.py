#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("resources.qrc", ".*logo-.*$")
    qt4.configure("clipgrab.pro")

def build():
    qt4.make()
    shelltools.chmod("icon.png", 0644)

def install():
    pisitools.dobin("clipgrab")
    pisitools.insinto("/usr/share/pixmaps/", "icon.png", "clipgrab.png")
    pisitools.dodoc("COPYING", "license.odt") 
