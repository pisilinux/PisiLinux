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
    pisitools.dosed("Makefile", "(?m)^(CC.*)gcc", r"\1%s" % get.CC())
    pisitools.dosed("Makefile", "(?m)^(LDFLAGS.*)-s", r"\1%s" % get.LDFLAGS())
    pisitools.dosed("Makefile", "(?m)^(CFLAGS.*)-O2", r"\1%s" % get.CFLAGS())

def build():
    autotools.make('STRIP=: CC="%s"' % get.CC())

def install():
    pisitools.dosbin("hdparm", "/sbin")
    pisitools.dosbin("contrib/idectl", "/sbin")

    pisitools.doman("hdparm.8")
    pisitools.dodoc("hdparm.lsm", "Changelog", "README.acoustic")
