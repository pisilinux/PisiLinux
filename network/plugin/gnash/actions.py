#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())
# to avoid sandbox violations - disabled temporary due to pisi ix error
#shelltools.system("gst-inspect")

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --disable-rpath \
                         --disable-jemalloc \
                         --disable-docbook \
                         --enable-python \
                         --enable-cygnal \
                         --enable-doublebuf \
                         --enable-renderer=all \
                         --enable-hwaccel=vaapi \
                         --enable-extensions=ALL \
                         --enable-media=gst \
                         --enable-gui=gtk,kde4,sdl,fb \
                         --with-plugins-install=system \
                         --with-gstpbutils-registry=/usr/lib/gstreamer-0.10 \
                         --with-gstpbutils-incl=/usr/include/gstreamer-0.10 \
                         --with-gstpbutils-lib=/usr/lib \
                         --with-npapi-plugindir=/usr/lib/browser-plugins \
                         ")
#                         --enable-media=ffmpeg,gst \

def build():
    autotools.make()

def install():
    autotools.rawInstall('install-plugins \
                          DESTDIR=%s \
                          INSTALL="install -p"' % get.installDIR())

    pisitools.dodoc("README", "COPYING")
