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

WorkDir = "psqlodbc-0%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-unixodbc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/lib/psqlodbcw.so", "psqlodbc.so")
    pisitools.remove("/usr/lib/psqlodbcw.la")
    pisitools.dodoc("license.txt", "readme.txt")
