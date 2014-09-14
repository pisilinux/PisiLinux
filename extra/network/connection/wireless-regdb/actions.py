#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

version = get.srcVERSION().split("_")[1]
WorkDir = "wireless-regdb-%s.%s.%s" % (version[:4], version[4:6], version[6:])
NoStrip = ["/"]

def install():
    pisitools.insinto("/usr/lib/crda", "regulatory.bin")

    pisitools.doman("regulatory.bin.5")
    pisitools.dodoc("README", "LICENSE")
