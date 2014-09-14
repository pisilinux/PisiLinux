#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("desktop", "GenericName=Photo Editor", "GenericName=Photo Editor\nComment[tr]=Dijital fotoğraf düzenleyici\nGenericName[tr]=Fotoğraf Düzenleyici")
    pisitools.dosed("Makefile", "/share/doc/fotoxx", "/share/doc/$(PF)")
    pisitools.dosed("Makefile", "xdg-desktop-menu", "#xdg-desktop-menu")
    autotools.make('PREFIX="/usr" \
                    CXXFLAGS="%s" \
                    LDFLAGS="%s"' % (get.CXXFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/", "icons/fotoxx.png")