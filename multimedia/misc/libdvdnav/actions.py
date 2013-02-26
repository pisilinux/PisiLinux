#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#
# taken from
# svn://svn.mplayerhq.hu/dvdnav/trunk/libdvdnav

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "libdvdnav"

def setup():
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-fi")

    autotools.configure("--with-libdvdcss=/usr \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("ChangeLog", "AUTHORS", "DEVELOPMENT-POLICY.txt", "README", "TODO", "doc/dvd_structures")

