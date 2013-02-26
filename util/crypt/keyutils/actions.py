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

def build():
    autotools.make("NO_ARLIB=1 LIBDIR=/lib USRLIBDIR=/usr/lib NO_GLIBC_KEYERR=1 CFLAGS=\"%s\"" % get.CFLAGS())

def install():
    autotools.install("NO_ARLIB=1 LIBDIR=/lib USRLIBDIR=/usr/lib DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENCE.GPL", "LICENCE.LGPL", "README")
