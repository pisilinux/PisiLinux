#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fomit-frame-pointer -ffast-math" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -fomit-frame-pointer -ffast-math" % get.CFLAGS())

    autotools.configure("--disable-static \
                         --enable-shared \
                         --enable-demos \
                         --with-trimesh=opcode \
                         --enable-new-trimesh \
                         --with-drawstuff=X11 \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG.txt", "README.txt")
