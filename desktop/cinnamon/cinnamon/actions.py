#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Cinnamon-1.6.7"
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh")
    #autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
			 --sysconfdir=/etc \
			 --libexecdir=/usr/lib/cinnamon \
			 --localstatedir=/var \
			 --disable-static \
			 --disable-schemas-compile \
			 --enable-compile-warnings=yes \
			 --with-session-tracking=systemd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "AUTHORS")
