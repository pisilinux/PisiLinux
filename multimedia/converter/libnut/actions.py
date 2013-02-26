#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# nut is done with checkouts from
# svn://svn.mplayerhq.hu/nut/src/trunk

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nut"

def build():
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.make("-j1 CC=%s" % get.CC())

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    pisitools.dodoc("COPYING", "README*")
