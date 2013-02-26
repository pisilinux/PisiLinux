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

shelltools.export("MONO_SHARED_DIR", get.workDIR())

def setup():
    autotools.configure("--disable-static\
                         --disable-rpath\
                         --enable-mono\
                         --enable-ipv6\
                         --enable-largefile")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    #pisitools.domove("/usr/bin/uuencode", "/usr/bin", "gmime-uuencode")
    #pisitools.domove("/usr/bin/uudecode", "/usr/bin", "gmime-uudecode")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "TODO")
