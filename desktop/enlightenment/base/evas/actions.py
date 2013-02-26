#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    autotools.configure("--enable-strict \
                         --disable-static \
                         --enable-fontconfig \
                         --enable-fribidi \
                         --enable-harfbuzz \
                         --disable-pixman \
                         --enable-buffer \
                         --disable-gl-sdl \
                         --enable-fb \
                         --enable-directfb \
                         --disable-wayland-shm \
                         --disable-wayland-egl \
                         --disable-sdl-primitive \
                         --disable-software-xcb \
                         --enable-software-xlib \
                         --disable-gl-xcb \
                         --enable-gl-xlib \
                         --disable-image-loader-edb \
                         --enable-image-loader-gif \
                         --enable-image-loader-tiff \
                         --disable-image-loader-svg \
                         --enable-image-loader-eet \
                         --disable-install-examples \
                         --disable-tests \
                         --disable-coverage \
                         --disable-doc \
                         --enable-evas-magic-debug \
                         --enable-static-software-generic \
                         --enable-buffer \
                         --enable-cpu-c \
                         --enable-scale-sample \
                         --enable-scale-smooth \
                         --enable-convert-8-rgb-332 \
                         --enable-convert-8-rgb-666 \
                         --enable-convert-8-rgb-232 \
                         --enable-convert-8-rgb-222 \
                         --enable-convert-8-rgb-221 \
                         --enable-convert-8-rgb-121 \
                         --enable-convert-8-rgb-111 \
                         --enable-convert-16-rgb-565 \
                         --enable-convert-16-rgb-555 \
                         --enable-convert-16-rgb-444 \
                         --enable-convert-16-rgb-rot-0 \
                         --enable-convert-16-rgb-rot-270 \
                         --enable-convert-16-rgb-rot-90 \
                         --enable-convert-24-rgb-888 \
                         --enable-convert-24-bgr-888 \
                         --enable-convert-32-rgb-8888 \
                         --enable-convert-32-rgbx-8888 \
                         --enable-convert-32-bgr-8888 \
                         --enable-convert-32-bgrx-8888 \
                         --enable-convert-32-rgb-rot-0 \
                         --enable-convert-32-rgb-rot-270 \
                         --enable-convert-32-rgb-rot-90 \
                         --disable-static-software-16 \
                         --disable-software-16-x11")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
