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

WorkDir = "w3c-libwww-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--without-mysql \
                         --enable-shared \
                         --disable-static \
                         --with-dav \
                         --with-md5 \
                         --with-zlib \
                         --with-expat \
                         --with-ssl \
                         --with-gnu-ld \
                         --with-regex")

def build():
    pisitools.dosed("Library/src/Makefile", "-L/usr/lib", "-L/usr/lib -L./.libs")
    autotools.make("-j1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dohtml("COPYRIGHT.html", "LICENSE.html", "PATCHES.html", "README.html")
    pisitools.dodoc("ChangeLog")
