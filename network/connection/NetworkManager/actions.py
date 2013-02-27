#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    # autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-wimax \
                         --enable-more-warnings=yes \
                         --with-crypto=nss \
                         --with-resolvconf=/etc/resolv.conf \
                         --with-iptables=/usr/sbin/iptables \
                         --with-systemdsystemunitdir=/lib/systemd/system")

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/NetworkManager/VPN")

    pisitools.dodoc("COPYING", "README")
