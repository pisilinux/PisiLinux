#!    pisitools.remove("/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

#shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DFORCED_UNBUNDLE=ON \
                    -DWITH_LQR=ON \
                    -DWITH_LENSFUN=ON \
                    -DWITH_MarbleWidget=ON \
                    -DENABLE_LCMS2=ON \
                    -DENABLE_INTERNALMYSQL=ON \
                    -DENABLE_KDEPIMLIBSSUPPORT=ON \
                    -DDIGIKAMSC_COMPILE_LIBMEDIAWIKI=ON \
                    -DDIGIKAMSC_USE_PRIVATE_SHAREDLIBS=ON \
                    -DDIGIKAMSC_COMPILE_LIBKGEOMAP=ON \
                    -DDIGIKAMSC_COMPILE_LIBKIPI=ON \
                    -DDIGIKAMSC_USE_PRIVATE_KDEGRAPHICS=OFF \
                    -DDIGIKAMSC_COMPILE_LIBMEDIAWIKI=OFF \
                    -DDIGIKAMSC_COMPILE_LIBKVKONTAKTE=OFF \
                    -DBUILD_tests=OFF ")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("NEWS", "README")

    pisitools.remove("/usr/share/locale/*/LC_MESSAGES/libkipi.mo")