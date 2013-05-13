#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-gnutls \
                         --with-openssl \
                         --enable-debug \
                         --with-ipv6 \
                         --disable-static \
                         --enable-rpath")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","NEWS","ChangeLog","README","THANKS","TODO","COPYING")
