#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # disable XAA to allow building against >=xorg-server-1.12.99.902
    # pisitools.dosed("configure.ac", ".*USE_XAA, 1.*")
    autotools.autoreconf("-vif")
    autotools.configure("\
                         --disable-static \
                         --enable-dri \
                        ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("COPYING", "ChangeLog", "README")
