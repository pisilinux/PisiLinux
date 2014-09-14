#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-i")
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/applications", "desktop/dreamchess.desktop")
    pisitools.insinto("/usr/share/pixmaps", "desktop/dreamchess.png")

    pisitools.dodoc("ChangeLog", "README", "NEWS", "COPYING", "AUTHORS")
