#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export('HOME', get.workDIR())

def setup():
    autotools.configure("--prefix=/usr \
                        --sysconfdir=/etc \
                        --disable-static \
                        --enable-pdf \
                        --enable-tiff \
                        --enable-djvu \
                        --enable-dvi \
                        --enable-t1lib \
                        --disable-nautilus \
                        --enable-comics \
                        --disable-scrollkeeper \
                        --disable-schemas-compile \
                        --enable-introspection")
                        #--enable-nautilus \ 
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING", "TODO")
