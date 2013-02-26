#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing -fno-force-addr -ffunction-sections -frename-registers -fomit-frame-pointer" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fno-strict-aliasing -fno-force-addr -ffunction-sections -frename-registers -fomit-frame-pointer" % get.CXXFLAGS())
    shelltools.export("CCASFLAGS","-Wa,--noexecstack")
    # to get rid of cvs
    shelltools.export("AUTOPOINT", "true")

    #libtools.libtoolize("--force --copy")
    autotools.autoreconf("-vfi")
    autotools.configure(" \
                      --prefix=/usr \
                      --mandir=/usr/share/man \
                      --disable-altivec \
                      --disable-artstest \
                      --disable-dxr3 \
                      --disable-vidix \
                      --enable-aalib \
                      --enable-asf \
                      --enable-directfb \
                      --enable-faad \
                      --enable-fb \
                      --enable-ffmpeg-popular-codecs \
                      --enable-ffmpeg-uncommon-codecs \
                      --enable-ipv6 \
                      --enable-mmap \
                      --enable-mng \
                      --enable-modplug \
                      --enable-opengl \
                      --enable-samba \
                      --enable-xinerama \
                      --with-external-a52dec \
                      --with-external-ffmpeg \
                      --with-external-libmad \
                      --with-internal-vcdlibs \
                      --with-vorbis \
                      --with-wavpack \
                      --with-x \
                      --with-xcb \
                      --with-xv-path=/usr/lib \
                      --without-esound \
                      --without-imagemagick \
                      --without-jack \
                      --disable-gdkpixbuf \
                      --disable-nls \
                      --disable-rpath \
                      --disable-syncfb \
                      --disable-optimizations \
                      --disable-dependency-tracking")
                      # the world is not ready for this code, see bug #8267
                      # --enable-antialiasing \
                      # --with-freetype \
                      # --with-fontconfig \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/xine-lib")

    pisitools.dohtml("doc/faq/faq.html", "doc/hackersguide/*.html", "doc/hackersguide/*.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "doc/README*", "doc/faq/faq.txt")

