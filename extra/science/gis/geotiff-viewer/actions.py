#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./configure prefix=/usr --disable-static LDFLAGS=-lm")

def build():
    autotools.make()

def install():
    pisitools.dobin("gtviewer")

    pisitools.insinto("/usr/share/applications", "gtviewer.desktop")
    pisitools.insinto("/usr/share/info", "gtviewer.info")
    pisitools.insinto("/usr/share/pixmaps", "gtviewer_logo.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "gtviewer.html", "gtviewer.txt")
