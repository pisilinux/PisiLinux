#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("-C src CFLAGS='%s -fPIC'" % get.CFLAGS())

def install():
    shelltools.cd("src")
    autotools.rawInstall("DESTDIR=%s LIBDIR=/usr/lib" % get.installDIR())
    shelltools.cd("..")

    pisitools.dodoc("README", "demo/demo.c")
