#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "volpack-%s" % get.srcVERSION().replace("_pre7","c7")

def setup():
    shelltools.export("CXXFLAGS", get.CXXFLAGS())
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.configure("--disable-dependency-tracking \
                         --enable-static=no")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

    #add examples
    pisitools.dodir("%s/%s/examples" % (get.docDIR(), get.srcNAME()))
    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()), "examples/.libs/*")
    pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()), "examples/brainsmall.den")
