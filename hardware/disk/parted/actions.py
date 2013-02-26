#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # FIXME: device-mapper is not in system.base discuss it
    autotools.configure("--disable-device-mapper \
                         --disable-static \
                         --without-readline \
                         --enable-Werror=no")

def build():
    autotools.make('CFLAGS="%s" CXXFLAGS="%s" CC="%s" CXX="%s"' %
            (get.CFLAGS(), get.CXXFLAGS(), get.CC(), get.CXX()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.dodoc("doc/API", "doc/USER.jp", "doc/FAT")

    #pisitools.removeDir("/usr/bin")
