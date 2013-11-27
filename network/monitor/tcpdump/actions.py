#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -O2 -DIP_MAX_MEMBERSHIPS=20" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-ipv6 \
                         --with-ssl \
                         --with-smi \
                         --disable-smb \
                         --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    pisitools.dosbin("tcpdump")

    pisitools.doman("tcpdump.1")
    pisitools.dodoc("CHANGES", "LICENSE", "CREDITS", "*.awk")
