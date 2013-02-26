#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-mmx \
                         --enable-sse \
                         --with-cairo \
                         --with-graphviz \
                         --with-pic \
                         --with-gio \
                         --with-gtk \
                         --with-gdk-pixbuf \
                         --with-libjpeg \
                         --with-libopenraw \
                         --includedir=/usr/include \
                         --datadir=/usr/share \
                         --with-libpng \
                         --with-jasper \
                         --with-librsvg \
                         --with-libspiro \
                         --with-libv4l \
                         --with-lua \
                         --with-exiv2 \
                         --with-umfpack \
                         --with-openexr \
                         --with-pango \
                         --with-pangocairo \
                         --with-sdl \
                         --disable-static \
                         --disable-gtk-doc \
                         --disable-workshop") # causes sandbox violations when enabled

def build():
    autotools.make()

# disabled due sandbox violations
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LESSER", "NEWS", "README")

