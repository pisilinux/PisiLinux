#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libfm-%s" % (get.srcVERSION())

def setup():
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --enable-debug \
                         --enable-udisks \
                         --enable-demo")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    pisitools.dosed("data/libfm.conf", "xarchiver", "file-roller")
    autotools.install()
    pisitools.dodoc("AUTHORS", "COPYING", "TODO")

