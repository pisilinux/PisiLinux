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
from pisi.actionsapi import get

def setup():
    autotools.configure('--enable-fbdev \
                         --enable-mmx \
                         --enable-sse \
                         --enable-jpeg \
                         --enable-png \
                         --enable-gif \
                         --enable-freetype \
                         --enable-multi \
                         --enable-sysfs \
                         --disable-sdl \
                         --disable-multi \
                         --disable-debug \
                         --disable-static \
                         --enable-zlib \
                         --enable-x11 \
                         --enable-video4linux \
                         --enable-video4linux2 \
                         --with-inputdrivers="all" \
                         --with-gfxdrivers="all" \
                         --disable-vnc')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("docs/html/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "TODO", "fb.modes")

