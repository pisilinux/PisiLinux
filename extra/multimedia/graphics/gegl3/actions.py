#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-mmx \
                         --enable-sse \
                         --includedir=/usr/include \
                         --datadir=/usr/share \
                         --with-pic \
                         --with-cairo \
                         --with-pango \
                         --with-pangocairo \
                         --with-gdk-pixbuf \
                         --with-lensfun \
                         --with-libjpeg \
                         --with-libpng \
                         --with-librsvg \
                         --with-openexr \
                         --with-sdl \
                         --with-libopenraw \
                         --with-jasper \
                         --with-graphviz \
                         --with-lua \
                         --with-libavformat \
                         --with-libv4l \
                         --with-libspiro \
                         --with-exiv2 \
                         --with-umfpack \
                         --disable-static \
                         --disable-gtk-doc \
                         --enable-gtk-doc-html=no \
                         --disable-docs \
                         --disable-workshop")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

# disabled due sandbox violations
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LESSER", "NEWS")

