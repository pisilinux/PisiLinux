#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd("source")

    autotools.configure(' --disable-native-texlive-build \
                          --with-banner-add=/PisiLinux \
                          --enable-cxx-runtime-hack \
                          --disable-all-pkgs \
                          --disable-dump-share \
                          --disable-ptex \
                          --enable-luatex  \
                          --enable-build-in-source-tree \
                          --without-system-ptexenc \
                          --with-system-graphite \
                          --without-system-icu \
                          --without-system-kpathsea \
                          --with-system-freetype2 \
                          --with-system-poppler \
                          --with-freetype2-libdir=/usr/lib \
                          --with-freetype2-include=/usr/include/freetype2 \
                          --with-system-gd \
                          --with-system-libpng \
                          --without-system-teckit \
                          --with-system-zlib \
                          --with-system-zziplib \
                          --with-system-t1lib \
                          --disable-shared \
                          --disable-largefile \
                          --disable-ipc \
                          --without-mf-x-toolkit \
                          --without-x')


def build():
    shelltools.cd("source")
    autotools.make()
    autotools.make("-C libs/zziplib")
    autotools.make("-C texk/web2c luatex")

def install():
    shelltools.cd("source")
    autotools.install()

    ## install luatex binary
    pisitools.dobin("texk/web2c/luatex")

    pisitools.dodoc("doc/texlive.pdf")