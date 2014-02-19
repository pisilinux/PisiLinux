# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-dbus \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/workrave \
                         --disable-pulse \
                         --enable-gconf \
                         --disable-gnome3 \
                         --disable-experimental \
                         --disable-xml")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("COPYING*", "AUTHORS*", "INSTALL", "NEWS*", "README*", "TODO")
