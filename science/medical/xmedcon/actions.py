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

def setup():
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --with-gnu-ld \
                         --enable-nifti \
                         --with-nifti-prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "etc/xmedcon.png")
    pisitools.dodoc("AUTHORS", "COPYING*", "INSTALL", "NEWS", "README", "REMARKS")
