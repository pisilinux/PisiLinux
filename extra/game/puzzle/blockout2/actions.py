#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "bl24_lin_src"
datadir = "/usr/share/blockout2"
mainsrc = "BlockOut"

def setup():
    pisitools.dosed("ImageLib/src/Makefile", "^CC.*gcc", "CC  = %s" % get.CC())
    pisitools.dosed("ImageLib/src/Makefile", "^CXX.*g\+\+", "CXX = %s" % get.CXX())
    pisitools.dosed("ImageLib/src/Makefile", "^CFLAGS[ ]*= \-O2", "CFLAGS    = %s " % get.CFLAGS())
    pisitools.dosed("ImageLib/src/Makefile", "^CXXFLAGS[ ]*= \-O2", "CXXFLAGS  = %s " % get.CXXFLAGS())

    pisitools.dosed("%s/Makefile" % mainsrc, "^CXX.*g\+\+", "CXX     = %s" % get.CXX())
    pisitools.dosed("%s/Makefile" % mainsrc, "-g -D_DEBUG", get.CXXFLAGS())
    pisitools.dosed("%s/Makefile" % mainsrc, "../ImageLib/src/libimagelib.a", "../ImageLib/src/libimagelib.a -lpng")

def build():
    shelltools.cd("ImageLib/src")
    autotools.make("-j1")
    shelltools.cd("../../%s" % mainsrc)
    autotools.make("-j1")

def install():
    pisitools.dodir(datadir)
    for d in ["images", "sounds"]:
        pisitools.insinto(datadir, "%s/%s" % (mainsrc, d))

    pisitools.dobin("%s/blockout2" % mainsrc)
