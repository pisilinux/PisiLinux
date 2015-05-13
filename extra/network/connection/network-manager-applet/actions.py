#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get


def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --disable-migration \
                         --disable-maintainer-mode \
                         --with-modem-manager-1 \
                         --with-bluetooth \
                         --without-gnome \
                         --enable-more-warnings=yes \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --prefix=/usr \
                         --libexecdir=/usr/lib/NetworkManager")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
