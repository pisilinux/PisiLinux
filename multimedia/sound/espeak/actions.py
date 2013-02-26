#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "espeak-%s-source" % get.srcVERSION()

def setup():
    # Build against portaudio v19
    shelltools.copy("src/portaudio19.h", "src/portaudio.h")

    # Remove binary voice dictionaries, we'll build them
    shelltools.system("rm -rf espeak-data/*_dict")

def build():
    autotools.make("-C src CXXFLAGS='%s' CFLAGS='%s' LDFLAGS='%s'" % (get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))

    shelltools.system("./compile-voices")

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s BINDIR=/usr/bin INCDIR=/usr/include/espeak LIBDIR=/usr/lib" % get.installDIR())
    shelltools.cd("..")

    pisitools.dodoc("ReadMe", "ChangeLog.txt", "License.txt")
