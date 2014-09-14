#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DFREETYPE_INCLUDE_DIR=/usr/include/freetype2 \
                          -DPODOFO_BUILD_SHARED=1 \
                          -DPODOFO_BUILD_STATIC=0 \
                          -DPODOFO_HAVE_JPEG_LIB=1 \
                          -DPODOFO_HAVE_PNG_LIB=1 \
                          -DPODOFO_HAVE_TIFF_LIB=1 \
                          -DWANT_FONTCONFIG=1 \
                          -DWANT_BOOST=1 \
                          -DUSE_STLPORT=1", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "TODO")
    pisitools.dohtml("README.html", "FAQ.html")
