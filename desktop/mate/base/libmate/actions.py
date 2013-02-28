#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

