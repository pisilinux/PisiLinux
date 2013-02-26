#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tinyxml"

major, minor = get.srcVERSION().split(".", 1)

def setup():
    pisitools.dosed("Makefile", "@MAJOR_V@", "%s" % major)
    pisitools.dosed("Makefile", "@MINOR_V@", "%s" % minor)

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/include", "*.h")
    # pisi dolib does not care for symlinks
    # pisitools.dolib("libtinyxml.so*")
    for i in shelltools.ls("libtinyxml.so*"):
        pisitools.insinto("/usr/lib/", i)

    pisitools.dodoc("changes.txt", "readme.txt")
    pisitools.dohtml("docs/*")
