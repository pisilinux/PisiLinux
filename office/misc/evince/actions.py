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
    shelltools.system("sed -i -e 's/gnome-icon-theme//' configure.ac configure")
    autotools.autoreconf("-vif")
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib/$_pkgalias \
                         --sysconfdir=/etc \
                         --localstatedir=/var \
                         --disable-maintainer-mode \
                         --disable-schemas-compile \
                         --disable-debug \
                         --disable-tests \
                         --disable-nautilus \
                         --enable-previewer \
                         --disable-introspection \
                         --enable-t1lib \
                         --enable-comics \
                         --disable-dvi \
                         --disable-ps \
                         --disable-djvu \
                         --disable-gtk-doc \
                         --without-keyring \
                         --with-smclient=xsmp")
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING", "TODO")
