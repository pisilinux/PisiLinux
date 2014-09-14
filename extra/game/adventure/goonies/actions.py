#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

datadir = "/usr/share/goonies"
datasources = ["graphics", "maps", "sound"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for d in datasources:
        fixperms(d)

    pisitools.dosed("Makefile", "^CC.*", "CC = %s" % get.CXX())
    pisitools.dosed("Makefile", "^CFLAGS.*", "CFLAGS = %s `sdl-config --cflags`" % get.CXXFLAGS())
    pisitools.dosed("Makefile", "^LDFLAGS.*", "LDFLAGS = %s `sdl-config --libs` -lSDL_image -lSDL_mixer -lSDL_sound -lGL -lGLU" % get.LDFLAGS().replace("-Wl,--as-needed", ""))
    pisitools.dosed("Makefile", "^STRIP.*", "STRIP = echo")

def build():
    autotools.make("-j1")

def install():
    pisitools.dobin("goonies")
    pisitools.dodir(datadir)

    for d in datasources:
        pisitools.insinto(datadir, d)

