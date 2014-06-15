#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-printing \
                         --enable-unicode-glyphs \
                         --with-wx-config=/usr/bin/wx-config-2.8")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/applications", "wxmaxima.desktop")
    pisitools.dosym("/usr/share/wxMaxima/wxmaxima.png", "/usr/share/pixmaps/wxmaxima.png")

    pisitools.remove("/usr/share/wxMaxima/COPYING")
    pisitools.remove("/usr/share/wxMaxima/README")

    pisitools.dodoc("NEWS", "AUTHORS", "ChangeLog", "README", "COPYING")
