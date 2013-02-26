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
  
    shelltools.system("./autogen.sh --prefix=/usr\
			 --sysconfdir=/etc \
			 --localstatedir=/var \
			 --disable-static \
			 --libexecdir=/usr/lib/mate-vfs \
			 --with-mateconf-source='xml::/etc/mateconf/mateconf.xml.defaults' \
			 --enable-ipv6 \
                         --enable-hal \
                         --enable-samba \
                         --enable-avahi \
                         --disable-selinux \
                         --disable-static \
                         --disable-schemas-install \
                         --disable-cdda \
                         --disable-fam \
                         --disable-howl")

def build():
    #shelltools.export("MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    pisitools.dodoc("TODO", "NEWS", "README", "COPYING", "AUTHORS", "ChangeLog")
