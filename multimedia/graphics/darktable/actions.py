#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.ldflags.add("-lgs")
    shelltools.makedirs("build")
    shelltools.cd("build")
    pisitools.cxxflags.add("-fpermissive")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DDONT_INSTALL_GCONF_SCHEMAS=True \
                          -DBINARY_PACKAGE_BUILD=1 \
                          -DUSE_GCONF_BACKEND=Off \
                          -DBUILD_USERMANUAL=False", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()
