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

WorkDir = "dmraid/%s" % get.srcVERSION().replace("_", ".")

def builddiet():
    autotools.make("distclean")
    shelltools.export("CC", "diet %s %s %s -Os -static" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))
    autotools.configure("--disable-libselinux \
                         --disable-libsepol")

    autotools.make("-j1")

    pisitools.insinto("/sbin/", "tools/dmraid", "dmraid.static")

def setup():
    autotools.configure("--enable-shared_lib")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #builddiet()
    pisitools.dodoc("CHANGELOG", "README", "TODO", "KNOWN_BUGS", "doc/*")
