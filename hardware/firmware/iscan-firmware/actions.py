#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/"]

def install():
    libdir = "usr/lib%s" % ("64" if get.ARCH() == "x86_64" else "")

    pisitools.insinto("/usr/lib/iscan", "%s/iscan/*" % libdir)
    pisitools.insinto("/usr/lib/esci", "%s/esci/*" % libdir)

    pisitools.insinto("/usr/share/esci", "usr/share/esci/*")
    pisitools.insinto("/usr/share/iscan", "usr/share/iscan/*")
    pisitools.insinto("/usr/share/iscan-data/device", "usr/share/iscan-data/device/*")

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "usr/share/doc/*")
