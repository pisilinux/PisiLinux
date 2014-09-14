#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    pisitools.cxxflags.add("-fpermissive")
    pisitools.dosed("plug-ins/postscript/diapsft2renderer.c", "freetype/ftglyph.h", "freetype2/ftglyph.h")
    pisitools.dosed("plug-ins/postscript/diapsft2renderer.c", "freetype/ftoutln.h", "freetype2/ftoutln.h")
    autotools.configure()
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
