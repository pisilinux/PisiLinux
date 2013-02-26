#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s" % get.ARCH()

def install():
    # Define bits variable for 32-bit and 64-bit architectures
    bits = "amd64" if get.ARCH() == "x86_64" else "i386"

    # Extract Debian package
    shelltools.system("ar -xv plexmediaserver_0.9.7.12.408-74b62af_%s.deb" % bits)

    shelltools.system("tar -xzvf data.tar.gz")

    pisitools.insinto("/usr/share/pixmaps/", "usr/share/pixmaps/plexmediamanager.png")
    pisitools.insinto("/usr/share/applications/", "usr/share/applications/plexmediamanager.desktop")
    pisitools.insinto("/", "etc")
    pisitools.insinto("/usr/", "usr/lib")
    pisitools.insinto("/usr/", "usr/sbin")

    shelltools.system("service apache start")
