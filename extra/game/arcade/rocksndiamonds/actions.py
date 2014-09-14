#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

gameDir = "/usr/share/rocksndiamonds"

def setup():
    pisitools.dosed("Makefile", "CC = gcc", "CC=%s" % get.CC())

def build():
    autotools.make("clean")
    autotools.make("sdl \
                    RO_GAME_DIR=%s \
                    RW_GAME_DIR=%s \
                    OPTIONS='%s'" % (gameDir, gameDir, get.CFLAGS()))

def install():
    pisitools.dobin("rocksndiamonds")

    for i in ["docs/elements", "graphics", "music", "levels", "sounds"]:
        pisitools.insinto("%s" % gameDir, i)

    pisitools.doman("rocksndiamonds.1")

    pisitools.dodoc("ChangeLog", "COPYING", "CREDITS", "README")
