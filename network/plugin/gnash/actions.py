#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
                         --disable-ghelp \
                         --disable-testsuite \
                         --without-swfdec-testsuite \
                         --without-ming \
                         --enable-python \
                         --enable-cygnal \
                         --enable-doublebuf \
                         --enable-renderer=all \
                         --enable-extensions=ALL \
                         --enable-media=gst \
                         --enable-gui=gtk,kde4,sdl,fb \
                         --with-plugins-install=system \
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
