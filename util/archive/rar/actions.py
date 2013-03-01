#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
