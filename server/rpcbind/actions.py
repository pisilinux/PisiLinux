#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fpie" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fpie" % get.LDFLAGS())

def setup():
    autotools.autoreconf("-vfi")
    ## glibc provides rpcinfo in /usr/sbin, so move it to /sbin, thus bindir=/sbin
    autotools.configure("--bindir=/sbin \
                         --enable-warmstarts \
                         --with-statedir=/var/lib/rpcbind \
                         --with-rpcuser=rpc \
                         --enable-libwrap")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/rpcbind")

    # glibc has rpcinfo.8, so avoid conflict with glibc
    pisitools.insinto("/usr/share/man/man8", "man/rpcinfo.8", "rpcbind-rpcinfo.8")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
