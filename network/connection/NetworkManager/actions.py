#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--disable-static \
                         --disable-silent-rules \
                         --disable-wimax \
                         --enable-more-warnings=yes \
                         --with-crypto=nss \
                         --with-resolvconf=/etc/resolv.conf \
                         --with-iptables=/usr/sbin/iptables \
                         --with-systemdsystemunitdir=/lib/systemd/system")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/NetworkManager/VPN")
    pisitools.dodir("/run/NetworkManager")
    pisitools.removeDir("/var/run")

    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTING", "COPYING", "NEWS", "README")
