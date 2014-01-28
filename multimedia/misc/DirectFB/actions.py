#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("docs/html/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "TODO", "fb.modes")

