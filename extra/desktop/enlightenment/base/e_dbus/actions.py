#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    autotools.configure("--prefix=/usr \
                        --disable-static \
                        --disable-ebluez \
                        --disable-econnman0_7x \
                        --disable-ehal \
                        --enable-enotify \
                        --disable-eofono \
                        --enable-eukit \
                        --disable-edbus-test \
                        --disable-edbus-test-client \
                        --disable-edbus-bluez-test \
                        --disable-edbus-connman0_7x-test \
                        --disable-edbus-ofono-test \
                        --disable-edbus-async-test \
                        --disable-edbus-performance-test \
                        --disable-doc")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README")
