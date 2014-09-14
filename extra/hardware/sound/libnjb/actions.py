#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/hal/fdi/information/10freedesktop/", "libnjb.fdi", "10-usb-music-players-libnjb.fdi")

    pisitools.removeDir("/usr/share/doc/libnjb-*")

    pisitools.dodoc("ChangeLog", "LICENSE", "FAQ", "README", "AUTHORS", "HACKING")
