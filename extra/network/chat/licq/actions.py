#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DUSE_OPENSSL=ON \
                          -DBUILD_PLUGINS=ON", sourceDir="..")


def build():
    shelltools.cd("build")
    cmaketools.make()


def install():
    shelltools.cd("build")
    cmaketools.install()
    shelltools.cd("..")

    # Licq-web plugin
    pisitools.dodir("/var/www/localhost/htdocs")
    pisitools.insinto("/var/www/localhost/htdocs/", "plugins/licqweb/")

    pisitools.dodoc("LICENSE", "README", "README.GPG", "README.OPENSSL", "doc/*")
