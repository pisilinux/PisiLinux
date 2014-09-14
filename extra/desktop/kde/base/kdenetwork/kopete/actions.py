#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

def setup():
    kde4.configure("-DWITH_JINGLE=TRUE -DMOZPLUGIN_INSTALL_DIR=/usr/lib/browser-plugins \
                    -DWITH_GOOGLETALK=ON \
                    -DWITH_Xmms=OFF \
                    -DWITH_LibMeanwhile=OFF \
                    -DWITH_qq=OFF \
                    -DCMAKE_BUILD_TYPE=Release \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DCMAKE_SKIP_RPATH=ON \
                    -Wno-dev")

def build():
    kde4.make()

def install():
    kde4.install()
    
    pisitools.dodoc("README", "INSTALL", "TODO", "COPYING*", "AUTHORS")
    
