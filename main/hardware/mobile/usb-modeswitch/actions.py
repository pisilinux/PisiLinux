#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

SNAPSHOT="20140529"

def build():
    autotools.make("CC='%s' CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
    autotools.rawInstall("-C usb-modeswitch-data-%s DESTDIR='%s'" % (SNAPSHOT, get.installDIR()))

    pisitools.removeDir("/etc/usb_modeswitch.d")

    pisitools.dodoc("README*", "COPYING")
