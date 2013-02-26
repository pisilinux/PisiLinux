#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#  cvs -d:pserver:anonymous@nogravity.cvs.sourceforge.net:/cvsroot/nogravity login
#  cvs -z3 -d:pserver:anonymous@nogravity.cvs.sourceforge.net:/cvsroot/nogravity co -P nogravity

WorkDir = "nogravity"

def setup():
    shelltools.export("LDFLAGS", "%s -lpng14 -lz" % get.LDFLAGS())
    shelltools.export("CFLAGS", "%s -I/usr/include/libpng14" % get.CFLAGS())
    shelltools.cd("src/Linux")
    shelltools.system("./bootstrap")
    autotools.configure("--enable-sound=sdl_mixer \
                         --disable-dependency-tracking \
                         --disable-opengl")

def build():
    shelltools.export("LDFLAGS", "%s -lpng14 -lz" % get.LDFLAGS())
    shelltools.export("CFLAGS", "%s -I/usr/include/libpng14" % get.CFLAGS())
    shelltools.cd("src/Linux")
    autotools.make()

def install():
    pisitools.dodir("/usr/share/nogravity")
    pisitools.dobin("src/Linux/nogravity", "/usr/share/nogravity")


