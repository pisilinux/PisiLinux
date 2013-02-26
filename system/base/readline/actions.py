#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #Force link to ncurses instead of tinfo, which we don't have, will be needed when we use as-needed ;)
    pisitools.dosed("support/shobj-conf", "SHLIB_LIBS='-ltinfo'", "SHLIB_LIBS=-lncurses")
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())

    options = "--with-curses \
               --libdir=/lib \
               --disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())
    
    if get.buildTYPE() == "emul32": return

    pisitools.removeDir("/usr/bin")

    pisitools.dohtml("doc/")
    pisitools.dodoc("CHANGELOG", "CHANGES", "README", "USAGE", "NEWS")
