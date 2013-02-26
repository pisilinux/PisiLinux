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

def setup():
    autotools.configure("--with-netpbm")
    pisitools.dosed("src/Makefile","LDFLAGS=.*", "LDFLAGS=-Lyes/lib %s" % get.LDFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          prefix=/usr \
                          exec_prefix=/usr" % get.installDIR())

    # Don't ship buggy Tcl/Tk frontend
    pisitools.remove("/usr/bin/gocr.tcl")

    pisitools.dodoc("AUTHORS", "HISTORY", "README", "BUGS", "CREDITS", "REVIEW")
