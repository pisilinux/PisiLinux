#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-libxml2 \
                         --with-expat \
                         --without-gssapi \
                         --without-libproxy \
                         --with-ssl=openssl \
                         --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt \
                         --enable-threadsafe-ssl=posix \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("THANKS", "TODO", "ChangeLog", "AUTHORS", "BUGS", "NEWS", "README", "doc/*.txt")
