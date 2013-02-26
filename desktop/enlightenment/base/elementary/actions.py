#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
#    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --enable-emap \
                         --enable-eweather \
                         --enable-quick-launch \
                         --enable-emotion \
                         --enable-ecore-x \
                         --enable-ecore-fb \
                         --disable-ecore-sdl \
                         --disable-ecore-wayland \
                         --disable-ecore-cocoa \
                         --disable-ecore-psl1ght \
                         --disable-ecore-win32 \
                         --disable-ecore-wince \
                         --enable-edbus \
                         --enable-efreet \
                         --enable-ethumb \
                         --disable-debug \
                         --disable-install-examples \
                         --disable-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")
