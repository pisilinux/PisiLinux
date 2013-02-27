#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "SDL_image-%s" % get.srcVERSION()

def setup():
    options = "--disable-dependency-tracking \
               --disable-static \
               --enable-gif \
               --enable-jpg \
               --enable-tif \
               --enable-png \
               --enable-pnm \
               --enable-bmp \
               --enable-xcf \
               --enable-xpm \
               --enable-tga \
               --enable-lbm \
               --enable-pcx \
               --disable-jpg-shared \
               --disable-png-shared \
               --disable-tif-shared"

    if get.buildTYPE() == "emul32":
        options += " --includedir=/usr/include \
                     --libdir=/usr/lib32"

        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())

    for i in ["NEWS", "AUTHORS", "ChangeLog"]:
        shelltools.touch(i)

    autotools.autoreconf("-vfi")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() != "emul32":
        pisitools.dobin(".libs/showimage")

    pisitools.dodoc("CHANGES", "COPYING", "README")
