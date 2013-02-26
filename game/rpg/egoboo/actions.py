#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "egoboo-%s" % get.srcVERSION()

data = "/usr/share/egoboo"

def setup():
    pisitools.dosed("src/game/Makefile", "-Os", get.CFLAGS())
    pisitools.dosed("src/game/Makefile", "= gcc", get.CC())
    #for f in docs:
    #    pisitools.dosed("game/%s" % f, "\r")

def build():
    autotools.make("-C src")

def install():
    #shelltools.chmod("src/game/egoboo", 0755)
    #pisitools.insinto(data, "src/game/egoboo")
    pisitools.dobin("src/game/egoboo")

    pisitools.insinto(data, "controls.txt")
    pisitools.insinto(data, "setup.txt")

