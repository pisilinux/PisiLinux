#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4
from pisi.actionsapi import get

NoStrip=["/usr/share"]

def setup():
    kde4.configure("-DKDE_DISTRIBUTION_TEXT='Pisi Linux' \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DWITH_SOLID_UDISKS2=ON \
                    -DWITH_FAM=OFF \
                    -DWITH_HUpnp=ON")

def build():
    kde4.make()

def install():
    kde4.install()

    #move Qt Designer plugins to Qt plugin directory
    pisitools.dodir("%s/designer" % qt4.plugindir)
    pisitools.domove("%s/plugins/designer/*" % kde4.modulesdir, "%s/designer" % qt4.plugindir)
    pisitools.removeDir("%s/plugins/designer" % kde4.modulesdir)

    #Use openssl CA list instead of the outdated KDE list
    pisitools.remove("%s/kssl/ca-bundle.crt" % kde4.appsdir)
    pisitools.dosym("/etc/ssl/certs/ca-certificates.crt", "%s/kssl/ca-bundle.crt" % kde4.appsdir)

    pisitools.dodoc("AUTHORS", "COPYING*", "README", "TODO")
