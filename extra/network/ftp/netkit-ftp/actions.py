#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --with-c-compiler=gcc \
                            --enable-ipv6")

    pisitools.dosed("MCONFIG", "^CC=.*", "CC=cc")
    pisitools.dosed("MCONFIG", "-O2", "%s -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    pisitools.dosed("MCONFIG", "^LDFLAGS=.*", "LDFLAGS=%s" % get.LDFLAGS())

    pisitools.dosed("MCONFIG", "^BINDIR=.*", "BINDIR=/usr/bin")
    pisitools.dosed("MCONFIG", "^MANDIR=.*", "MANDIR=/usr/share/man")
    pisitools.dosed("MCONFIG", "^SBINDIR=.*", "SBINDIR=/usr/sbin")


def build():
    autotools.make('CC="%s" LDFLAGS="%s"' % (get.CC(), get.LDFLAGS()))

def install():
    autotools.rawInstall("INSTALLROOT=%s" % get.installDIR())
    pisitools.remove("/usr/bin/pftp")

    pisitools.dodoc("ChangeLog", "README", "BUGS")
