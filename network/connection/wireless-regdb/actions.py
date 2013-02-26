#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

version = get.srcVERSION().split("_")[1]
WorkDir = "wireless-regdb-%s.%s.%s" % (version[:4], version[4:6], version[6:])
NoStrip = ["/"]

def install():
    pisitools.insinto("/usr/lib/crda", "regulatory.bin")

    pisitools.doman("regulatory.bin.5")
    pisitools.dodoc("README", "LICENSE")
