#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("NO_ARLIB=1 LIBDIR=/lib USRLIBDIR=/usr/lib NO_GLIBC_KEYERR=1 CFLAGS=\"%s\"" % get.CFLAGS())

def install():
    autotools.install("NO_ARLIB=1 LIBDIR=/lib USRLIBDIR=/usr/lib DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENCE.GPL", "LICENCE.LGPL", "README")
