#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -lz" % get.LDFLAGS())
    shelltools.system("sed -i -e '/^lxdream_LDADD =/s|=|= -lz|g' src/Makefile.in || exit 1") 
    autotools.autoconf()

    autotools.configure(" --prefix=/usr \
                          --with-gtk \
                          --sysconfdir=/etc \
                          --with-sdl \
                          --without-esd \
                          --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
