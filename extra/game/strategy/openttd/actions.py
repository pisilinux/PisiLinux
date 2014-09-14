#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.rawConfigure('--prefix-dir="/%s" \
                            --binary-dir="bin" \
                            --data-dir="share/%s" \
                            --icon-dir="share/pixmaps" \
                            --icon-theme-dir="share/icons/hicolor" \
                            --man-dir="share/man/man6" \
                            --menu-dir="share/applications" \
                            --doc-dir="share/doc/%s" \
                            --install-dir="%s" \
                            --disable-strip \
                            --enable-lto \
                            --menu-group="Game;StrategyGame;" \
                            --without-allegro \
                            --with-sdl \
                            --with-zlib \
                            --with-liblzo2 \
                            --with-png \
                            --with-freetype \
                            --with-fontconfig \
                            --with-icu \
                            --without-iconv \
                            ' % (get.defaultprefixDIR(),
                                 get.srcNAME(),
                                 get.srcNAME(),
                                 get.installDIR()
                            ))

def build():
    autotools.make()

def install():
    autotools.install()
#    pisitools.removeDir("/%s/share/pixmaps" % get.defaultprefixDIR())
