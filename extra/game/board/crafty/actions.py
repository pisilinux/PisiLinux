#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

arch = get.ARCH()

def setup():
    pisitools.dosed("Makefile", "-lpthread", "-pthread")
    pisitools.dosed("Makefile", "CC=gcc CXX=g\+\+", "CC=%s CXX=%s" % (get.CC(), get.CXX()))
    if arch == "i686":
        pisitools.dosed("Makefile", "-DINLINE64", "-DINLINE32")

def build():
    autotools.make("linux")

def install():
    pisitools.dosym("/usr/share/crafty/crafty", "/usr/bin/crafty")
    pisitools.dodir("/usr/share/crafty")
    pisitools.dobin("crafty", "/usr/share/crafty")
    pisitools.insinto("/usr/share/crafty", "crafty.hlp")