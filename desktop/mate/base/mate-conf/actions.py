#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
			--libexecdir=/usr/lib/MateConf \
			--localstatedir=/var \
			--disable-static \
			--enable-defaults-service \
			--enable-gsettings-backend=yes \
			--enable-introspection \
			--disable-gtk-doc \
			--enable-deprecation-flags")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
