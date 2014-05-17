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
                    -DCMAKE_SKIP_RPATH=ON \
                    -Wno-dev")

def build():
    kde4.make()

def install():
    kde4.install()
    
    # fix for package-manager
    pisitools.dosym("/usr/share/icons/nuvola/16x16/actions/list-add.png", "/usr/share/icons/nuvola/16x16/actions/add.png")
    pisitools.dosym("/usr/share/icons/nuvola/22x22/actions/list-add.png", "/usr/share/icons/nuvola/22x22/actions/add.png")
    pisitools.dosym("/usr/share/icons/nuvola/32x32/actions/list-add.png", "/usr/share/icons/nuvola/32x32/actions/add.png")
    pisitools.dosym("/usr/share/icons/nuvola/48x48/actions/list-add.png", "/usr/share/icons/nuvola/48x48/actions/add.png")

    pisitools.dodoc("COPYING*", "README")
