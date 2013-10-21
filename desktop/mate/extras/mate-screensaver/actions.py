#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure(" --enable-locking \
                          --with-xf86gamma-ext \
                          --with-kbd-layout-indicator \
                          --with-systemd=no \
                          --prefix=/usr \
                          --sysconfdir=/etc \
                          --libexecdir=/usr/lib \
                          --without-console-kit \
                          --with-xscreensaverdir=/usr/share/xscreensaver/config \
                          --with-xscreensaverhackdir=/usr/lib/misc/xscreensaver")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")