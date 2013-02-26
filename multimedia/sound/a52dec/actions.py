#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-djbfft")

def build():
    autotools.make('CFLAGS="%s"' % get.CFLAGS())

def install():
    autotools.rawInstall('DESTDIR="%s" docdir=/%s/%s/html' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.insinto("/usr/include/a52dec", "liba52/a52_internal.h")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "doc/liba52.txt")
