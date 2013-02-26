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

WorkDir = "splix"

def build():
    shelltools.export("OS_CFLAGS", get.CFLAGS())
    shelltools.export("OS_LDFLAGS", get.LDFLAGS())
    shelltools.export("OS_CXXFLAGS", "%s -fno-strict-aliasing" % get.CXXFLAGS())

    shelltools.makedirs("ppd")
    autotools.make("-C ppd ppd")

    autotools.make("V=1")

def install():
    autotools.install("DESTDIR=%s CUPSPPD=/usr/share/cups/model/splix" % get.installDIR())

    # Install color profiles
    pisitools.insinto("/usr/share/cups/model/samsung/cms", "cms/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS", "TODO")
