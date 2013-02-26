#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

NoStrip = ["/"]
WorkDir = get.ARCH()
lib_dir = "lib64" if get.ARCH() == "x86_64" else "lib"

def install():
    pisitools.dobin("usr/bin/*")
    pisitools.dolib_so("usr/%s/*" % lib_dir)

    pisitools.insinto("/usr/include", "usr/include/*")

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "usr/local/Cg/docs/*")

    for man in ("man1", "man3", "manCg", "manCgFX"):
        pisitools.doman("usr/share/man/%s/*" % man)
