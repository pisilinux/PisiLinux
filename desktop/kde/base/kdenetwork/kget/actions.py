#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

def setup():
    kde4.configure("-DCMAKE_BUILD_TYPE=Release \
                    -DKDE4_BUILD_TESTS=OFF \
                    -DWITH_NepomukCore=OFF \
                    -DWITH_NepomukWidgets=OFF \
                    -Wno-dev")

def build():
    kde4.make()

def install():
    kde4.install()
    
    pisitools.dodoc("AUTHORS", "Changelog", "COPYING*", "README", "TODO")
