#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fstack-protector-all" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-dbus \
                         --enable-cyrus-sasl \
                         --enable-gnutls=yes \
                         --enable-nss=yes \
                         --enable-nm \
                         --enable-cap \
                         --enable-mono \
                         --disable-schemas-install \
                         --disable-meanwhile \
                         --enable-nm \
                         --enable-tcl \
                         --enable-tk \
                         --x-includes=/usr/include/X11 \
                         --with-gnutls-includes=/usr/include/gnutls \
                         --with-gnutls-libs=/usr/lib")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("../icons/hicolor/48x48/apps/pidgin.png", "/usr/share/pixmaps/pidgin.png")

    pisitools.dodoc("AUTHORS", "COPYING", "HACKING", "NEWS", "README", "ChangeLog")

    perlmodules.removePodfiles()
