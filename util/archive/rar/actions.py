#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s/%s" % (get.ARCH(), get.srcNAME())
NoStrip = ["/"]

def install():
    pisitools.insinto("/opt/rar/bin", "rar")
    pisitools.insinto("/opt/rar/lib", "default.sfx")
    pisitools.insinto("/opt/rar/etc", "rarfiles.lst")

    pisitools.dosym("/opt/rar/bin/rar", "/usr/bin/rar")

    pisitools.dodoc("license.txt", "readme.txt", "whatsnew.txt", "order.htm", "rar.txt")
