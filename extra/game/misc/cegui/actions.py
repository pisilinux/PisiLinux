#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "lib64", "lib")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCEGUI_LIB_INSTALL_DIR=lib \
                          -DCEGUI_SAMPLES_USE_DIRECTFB=OFF \
                          -DCEGUI_BUILD_PYTHON_MODULES=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/PCRE-LICENSE")
