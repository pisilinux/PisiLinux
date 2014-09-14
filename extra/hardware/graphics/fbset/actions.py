#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "^CC =.*", "CC = %s -Wall -I. %s" % (get.CC(), get.CFLAGS()))
    pisitools.dosed("Makefile", "^modes.tab.c", "modes.tab.h modes.tab.c")

    pisitools.dosed("etc/fb.modes.ATI", "geometry 10224 768 10224 768 8", "geometry 1024 768 1024 768 8")
    pisitools.dosed("etc/fb.modes.ATI", "geometry 1024 1024 1024 1024 8", "geometry 1280 1024 1280 1024 8")


def build():
    autotools.make("-j1")

def install():
    pisitools.dobin("fbset")
    pisitools.dobin("modeline2fb")
    pisitools.doman("fb.modes.5", "fbset.8")
    pisitools.dodoc("etc/fb.modes.*")


