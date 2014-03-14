# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")

    autotools.configure("--disable-static \
                         --enable-unix-transport \
                         --enable-tcp-transport \
                         --enable-local-transport \
                         --enable-secure-rpc \
                         --enable-xpm-logos \
                         --enable-xdm-auth \
                         --with-pam \
                         --with-xdmconfigdir=/etc/X11/xdm \
                         --with-default-vt=vt7 \
                         --with-config-type=ws \
                         --with-xft \
                         --with-pixmapdir=/usr/share/X11/xdm/pixmaps \
                        ")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/xdm")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
