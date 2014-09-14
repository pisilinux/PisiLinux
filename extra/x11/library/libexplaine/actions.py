#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get



def setup():
    skiptests=["t0555a","t0524a"]
    for t in skiptests:
        shelltools.system('sed -i "s/\([ \t]\)$t\([ \t]\)/\1/g" Makefile.in')
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("BUILDING", "LICENSE", "README")

 
