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
    pisitools.dosed("GNUmakefile","CC *=.*","CC = %s" % get.CC())
    pisitools.dosed("GNUmakefile","CFLAGS= ","CFLAGS= %s " % get.CFLAGS())

def build():
    autotools.make()

def install():
    for i in ["avcdelete", "avcexport", "avcimport",
              "avctest", "ex_avcwrite"]:
        pisitools.dobin(i)

    pisitools.dodoc("avce00.html", "dbf_api.html")
