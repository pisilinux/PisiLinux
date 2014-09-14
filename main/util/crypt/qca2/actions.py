#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --datadir=/usr/share \
                            --no-separate-debug-info \
                            --release \
                            --certstore-path=/etc/ssl/certs/ca-certificates.crt")

def build():
    autotools.make()
    autotools.make("apidox")

def install():
    # Remove source build directory variable
    pisitools.dosed("lib/libqca.prl", "^QMAKE_PRL_BUILD_DIR.*$")

    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Put apidocs in its own directory
    pisitools.dodir("/usr/share/doc/qca2-apidocs/html")
    pisitools.insinto("/usr/share/doc/qca2-apidocs/html", "apidocs/html/*")

    pisitools.dodoc("README", "TODO", "COPYING")
