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

#WorkDir = "palp"

def build():
    pisitools.dosed("GNUmakefile", "^CFLAGS=.*$", "CFLAGS=%s" % get.CFLAGS())
    autotools.make("CC=%s" % get.CC())

def install():
    for exe in shelltools.ls("*.x"):
        pisitools.dobin(exe)
        pisitools.rename("/usr/bin/%s" % exe, "palp-%s" % exe)

    pisitools.dodoc("COPYING")
