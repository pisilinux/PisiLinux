#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s+-%s" % (get.srcNAME(), get.srcVERSION())
docompile = False if get.ARCH() == "x86_64" else True

def setup():
    pisitools.dosed("memtest.lds", "0x5000", "0x100000")

def build():
    if docompile:
        autotools.make()

def install():
    if docompile:
        finalbin = "memtest.bin"
    else:
        finalbin = "precomp.bin"

    pisitools.insinto("/boot", finalbin, "memtest")

    pisitools.dodoc("FAQ", "README*")

