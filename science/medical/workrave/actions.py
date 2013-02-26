# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

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

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("COPYING*", "AUTHORS*", "INSTALL", "NEWS*", "README*", "TODO")
