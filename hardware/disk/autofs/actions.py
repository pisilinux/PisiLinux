#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-mount-locking \
                         --enable-ignore-busy \
                         --disable-mount-move \
                         --with-sasl=yes \
                         --with-systemd \
                         --without-hesiod \
                         --with-fifodir=/var/run/autofs \
                         --with-flagdir=/var/run/autofs \
                         --with-libtirpc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALLROOT=%s" % get.installDIR())

    #pisitools.removeDir("/etc/init.d")

    pisitools.dodoc("CREDITS", "COPY*", "samples/ldap*", "samples/autofs.schema")
