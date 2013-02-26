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

def setup():
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --with-udev-rules=69-libmtp.rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #install HAL file for portable audio players
    pisitools.insinto("/usr/share/hal/fdi/information/10freedesktop", "libmtp.fdi", "10-usb-music-players-libmtp.fdi")

    #rename UDEV rules
    #pisitools.rename("/lib/udev/rules.d/libmtp.rules", "69-libmtp.rules")

    #pisitools.removeDir("/usr/share/doc/libmtp-*")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "AUTHORS", "TODO")
