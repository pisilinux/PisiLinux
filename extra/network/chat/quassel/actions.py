#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    kde4.configure("-DWANT_MONO=ON \
                    -DWANT_CORE=ON \
                    -DWANT_QTCLIENT=ON \
                    -DWITH_OPENSSL=ON \
                    -DWITH_WEBKIT=ON \
                    -DWITH_PHONON=ON \
                    -DWITH_KDE=ON \
                    -DWITH_OXYGEN=ON \
                    -DWITH_LIBINDICATE=OFF \
                    -DEMBED_DATA=OFF \
                    -DDATA_INSTALL_DIR=/usr/share/kde4/apps")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodir("/var/cache/quassel")
    shelltools.chmod("%s/var/cache/quassel" % get.installDIR(), 0770)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "gpl-?.0.txt")
