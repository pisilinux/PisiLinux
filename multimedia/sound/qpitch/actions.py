#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/CMakeLists.txt", "xpm", "png")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

    shelltools.system("doxygen")

def install():
    cmaketools.install()

    pisitools.dohtml("docs/html/*")
    pisitools.dodoc("COPYING", "README", "changelog")
