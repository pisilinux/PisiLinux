#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="lynx2-8-7"

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --with-ssl \
                         --enable-nls \
                         --enable-ipv6 \
                         --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS*", "AUTHORS", "CHANGES", "COPYING", "INSTALLATION","README")

    pisitools.dobin("lynx")
