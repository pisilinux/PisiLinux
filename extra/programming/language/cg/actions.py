#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
