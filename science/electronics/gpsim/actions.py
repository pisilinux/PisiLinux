#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--prefix=/usr")
    
    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ") 
    
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING", "NEWS", "PROCESSORS", "README", "README.*", "TODO")
    pisitools.dodoc("doc/gpsim.*")
