#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get


def setup():
    shelltools.export("LDFLAGS","%s -lX11" % get.LDFLAGS())
    kde4.configure("-DCMAKE_BUILD_TYPE=Release \
		    -DCMAKE_INSTALL_PREFIX=/usr \
		    -DLIB_INSTALL_DIR=/usr/lib \
		    -DSYSCONF_INSTALL_DIR=/etc \
		    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
		    -DBUILD_TESTING=OFF \
		    -DWITH_Nepomuk=OFF \
		    -DLINK_LIBRARIES=-lX11")
    
def build():
    kde4.make()

def install():
    kde4.install()
    
    pisitools.dodoc("AUTHORS", "COPYING", "README")
