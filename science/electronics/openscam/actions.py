#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    pisitools.dosed("src/openscam/view/GLFreeType.cpp", "freetype/freetype.h", "freetype2/freetype.h")
    pisitools.dosed("src/openscam/view/GLFreeType.cpp", "freetype/ftglyph.h", "freetype2/ftglyph.h")
    pisitools.dosed("src/openscam/view/GLFreeType.cpp", "freetype/ftoutln.h", "freetype2/ftoutln.h")
    pisitools.dosed("src/openscam/view/GLFreeType.cpp", "freetype/fttrigon.h", "freetype2/fttrigon.h")
    scons.make("-C cbang compiler=gnu")
    scons.make("compiler=gnu")
    
def install():
    scons.install("install compiler=gnu install_prefix=%s/usr" % get.installDIR())