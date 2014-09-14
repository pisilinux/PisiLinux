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
    pisitools.dosed("app/text/gimpfont.c", "freetype/tttables.h", "freetype2/tttables.h")
    autotools.autoreconf("-fi")
    autotools.configure("--without-webkit \
                         --disable-gtk-doc \
                         --disable-altivec \
                         --disable-alsatest \
                         --enable-python \
                         --enable-default-binary \
                         --enable-mmx \
                         --enable-sse \
                         --enable-mp \
                         --with-linux-input \
                         --with-poppler \
                         --with-libjpeg \
                         --with-libexif \
                         --with-librsvg \
                         --with-libtiff \
                         --with-libmng \
                         --with-libpng \
                         --with-webkit \
                         --with-lcms \
                         --with-alsa \
                         --with-dbus \
                         --with-aa \
                         --with-x")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # Add illustrator and other mime types
    pisitools.dosed("desktop/gimp.desktop.in", "^MimeType=application/postscript;application/pdf;(.*)$",
                    "MimeType=\\1;image/x-sun-raster;image/x-gray;image/x-pcx;image/jpg;image/x-bmp;image/pjpeg;image/x-png;application/illustrator;")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README", "INSTALL", "LICENSE")