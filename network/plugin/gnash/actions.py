#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    
    shelltools.export("LDFLAGS","-lboost_system")
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
                         --without-gconf \
                         --with-npapi-incl=/usr/include/npapi-sdk \
                         --with-npapi-plugindir=/usr/lib/browser-plugins \
                         ")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('install-plugins \
                          DESTDIR=%s \
                          INSTALL="install -p"' % get.installDIR())

    pisitools.dodoc("README", "COPYING")
