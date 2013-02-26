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

def setup():
    shelltools.system("./autogen.sh  --sysconfdir=/etc \
				     --localstatedir=/var \
				     --libexecdir=/usr/lib/libmate \
				     --with-mateconf-source='xml::/etc/mateconf/mateconf.xml.defaults' \
				     --disable-static \
				     --disable-esd \
				     --disable-schemas-install \
				     --enable-gtk-doc \
				     --enable-canberra")
    autotools.configure()
    
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("NEWS", "MAINTAINERS", "README", "ChangeLog", "AUTHORS")

