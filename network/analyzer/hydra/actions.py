#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "hydra-%s-src" % get.srcVERSION()

moduleconfig = {"XDEFINES": "-DLIBOPENSSL -DLIBSSH",
                "XLIBS": "-lcrypto -lssl -lssh -lm",
                "XLIBPATHS": "",
                "XIPATHS": "",
                "CC": get.CC(),
                "STRIP": "true"
}


def setup():
    pisitools.dosed("Makefile.am", "-O2", get.CFLAGS())
    autotools.configure("--disable-xhydra")

#    for i in moduleconfig:
#        pisitools.dosed("Makefile", "^%s=.*" % i, "%s=%s" % (i, moduleconfig[i]))

def build():
    autotools.make()

def install():
    for i in ["hydra", "pw-inspector"]:
        pisitools.dobin(i)

    pisitools.dodoc("CHANGES", "LICENSE*", "README*")
