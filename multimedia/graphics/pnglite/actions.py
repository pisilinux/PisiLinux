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

WorkDir = "."

def build():
    autotools.compile("%s -shared -fPIC -Wl,--soname,libpnglite.so.0 -o libpnglite.so.0.1 pnglite.c -lz" % get.LDFLAGS())

def install():
    pisitools.insinto("/usr/include", "pnglite.h")
    shelltools.chmod("%s/usr/include/pnglite.h" % get.installDIR(), 0644)

    pisitools.insinto("/usr/lib", "libpnglite.so.0.1")
    pisitools.dosym("libpnglite.so.0.1", "/usr/lib/libpnglite.so.0")
    pisitools.dosym("libpnglite.so.0", "/usr/lib/libpnglite.so")
