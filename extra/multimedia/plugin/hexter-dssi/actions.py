#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("CC=%s LDFLAGS=\"%s\" CFLAGS=\"%s\"" % (get.CC(), get.LDFLAGS(), get.CFLAGS()))

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("jack-dssi-host", "/usr/bin/hexter")
    pisitools.dodoc("README", "TODO", "AUTHORS")