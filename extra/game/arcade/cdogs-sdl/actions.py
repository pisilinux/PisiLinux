#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os


def setup():
    pisitools.dosed("src/Makefile", "^CF_OPTIMISE.*", 'CF_OPTIMISE +=  `sdl-config --cflags`')
    pisitools.dosed("src/Makefile", "^LDFLAGS.*", 'LDFLAGS = `sdl-config --libs` -lSDL_mixer')
    pisitools.dosed("src/Makefile", " -w", " -Wall")
    pisitools.dosed("src/Makefile", "strip", "echo")

def build():
    shelltools.cd("src")
    autotools.make('I_AM_CONFIGURED=yes \
                    SYSTEM=linux \
                    PREFIX=/usr/ \
                    BINDIR=/usr/bin/ \
                    DATADIR=/usr/share/cdogs-sdl/ \
                    DESTDIR="%s" \
                    cdogs' % get.installDIR())

def install():
    pisitools.dobin("src/cdogs")
    pisitools.rename("/usr/bin/cdogs", "cdogs-sdl")

    pisitools.dodoc("doc/AUTHORS", "doc/COPYING", "doc/original_readme.txt", "doc/README_DATA", "doc/ChangeLog", "doc/README", "doc/TODO")
