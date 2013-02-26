#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-vfi")
    libtools.libtoolize("--copy --force")

    shelltools.export("CFLAGS", "%s -DDCT_YUV_PRECISION=1" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -DDCT_YUV_PRECISION=1" % get.CXXFLAGS())

    autotools.configure("--enable-deprecated \
                         --enable-experimental \
                         --enable-mmx \
                         --enable-3dnow \
                         --enable-sse \
                         --enable-sse2 \
                         --enable-freetype2 \
                         --enable-libv4l2 \
                         --enable-libv4lconvert \
                         --enable-v4l \
                         --enable-lame \
                         --enable-x264 \
                         --enable-xvid \
                         --enable-ogg \
                         --enable-vorbis \
                         --enable-theora \
                         --enable-libdvdread \
                         --enable-libdv \
                         --enable-libquicktime \
                         --enable-lzo \
                         --enable-a52 \
                         --enable-libmpeg2 \
                         --enable-libmpeg2convert \
                         --enable-libxml2 \
                         --enable-mjpegtools \
                         --enable-nuv \
                         --enable-sdl \
                         --enable-imagemagick \
                         --enable-libjpeg \
                         --with-mod-path=/usr/lib/transcode \
                         --with-x \
                         --with-lzo-includes=/usr/include/lzo \
                         ")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")

