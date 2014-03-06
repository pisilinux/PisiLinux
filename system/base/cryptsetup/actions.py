#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static\
                         --sbindir=/sbin \
                         --libdir=/lib \
                         --disable-rpath\
                         --enable-python")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/lib/pkgconfig", "/usr/lib")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*",
                    "FAQ", "README*", "NEWS", "TODO")
