# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-bittorrent \
                         --enable-metalink \
                         --enable-epoll \
                         --enable-nls \
                         --disable-rpath \
                         --with-gnutls \
                         --with-openssl \
                         --with-sqlite3 \
                         --with-libxml2 \
                         --with-libcares \
                         --with-libz \
                         --with-ca-bundle=/etc/pki/tls/certs/ca-bundle.crt")

def build():
    autotools.make("-C po update-gmo")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
