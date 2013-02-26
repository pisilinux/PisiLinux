#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fstack-protector-all" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-ipv6 \
                         --with-libsmi \
                         --with-gnu-ld \
                         --with-pic \
                         --with-adns=no \
                         --with-ssl \
                         --with-libcap \
                         --disable-warnings-as-errors \
                         --with-python \
                         --with-plugins=/usr/lib/wireshark/plugins")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "image/hi48-app-wireshark.png", "wireshark.png")
    pisitools.insinto("/usr/share/applications/", "wireshark.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
