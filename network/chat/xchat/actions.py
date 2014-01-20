#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # xchat sourcecode ships with po/Makefile.in.in from gettext-0.17
    # which fails with >= gettext-0.18
    shelltools.system("cp /usr/share/gettext/po/Makefile.in.in %s/%s/po" % (get.workDIR(), get.srcDIR()))

    autotools.autoreconf("-vif")
    autotools.configure("--enable-shm \
                         --enable-ipv6 \
                         --enable-openssl \
                         --disable-rpath \
                         --enable-spell=libsexy")
    
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")    

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "HACKING", "README")
