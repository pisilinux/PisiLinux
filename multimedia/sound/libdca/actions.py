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
    autotools.autoreconf("-fi")
    autotools.configure("--enable-shared \
                         --enable-oss \
                         --disable-static")

def build():
    autotools.make('OPT_CFLAGS=""')

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.remove("/usr/lib/*.a")

    # FIXME: avidemux needs this
    # pisitools.insinto("/usr/include","libdts/dca_internal.h")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO", "doc/libdca.txt")

