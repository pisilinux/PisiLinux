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


def setup():
    kde4.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DENABLE_LCMS2=ON \
                    -DImageMagick_MagickCore_LIBRARY=/usr/lib/libMagickCore-6.Q16HDRI.so \
                    -DDIGIKAMSC_USE_PRIVATE_KDEGRAPHICS=OFF")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("NEWS", "README")

    pisitools.remove("/usr/share/locale/*/LC_MESSAGES/libkipi.mo")