#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    #sandbox error fixed
    pisitools.dosed("data/dconf/Makefile.am", "dconf update", "")
    pisitools.dosed("data/dconf/Makefile.in", "dconf update", "")
    
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/ibus \
                         --enable-gconf \
                         --enable-dconf \
                         --enable-vala \
                         --enable-ui \
                         --enable-gtk-doc \
                         --enable-python-library \
                         --enable-gtk3 \
                         --enable-gtk2")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")