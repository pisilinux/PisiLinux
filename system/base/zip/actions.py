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

WorkDir="%s30" % get.srcNAME()

def build():
    autotools.make("-f unix/Makefile CC=%s CPP=%s generic" % (get.CC(), get.CXX()))

def install():
    for bin in ["zip","zipcloak","zipnote","zipsplit"]:
        pisitools.dobin(bin)

    pisitools.doman("man/*.1")
    pisitools.dodoc("BUGS", "CHANGES", "LICENSE", "README", "TODO", "WHATSNEW", "WHERE")
