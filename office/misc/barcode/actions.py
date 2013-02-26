#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

    pisitools.dosed("Makefile", "/info", "/share/info")
    pisitools.dosed("Makefile", "/man/", "/share/man/")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/lib")
    pisitools.dodoc("ChangeLog", "README", "TODO", "doc/barcode.pdf")
