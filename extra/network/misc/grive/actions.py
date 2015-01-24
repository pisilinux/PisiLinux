#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i -e '/find_package(BFD)/d' libgrive/CMakeLists.txt")
    shelltools.system("sed -i -e '43d' bgrive/CMakeLists.txt")
    shelltools.system("sed -i '9s|json/json.h|json-c/json.h|g' cmake/Modules/FindJSONC.cmake")
    shelltools.system("sed -i '10s|json|json-c json|g' cmake/Modules/FindJSONC.cmake")
    shelltools.system("sed -i '32s|json/json_tokener.h|json-c/json_tokener.h|g' libgrive/src/protocol/Json.cc")
    shelltools.system("sed -i '33s|json/linkhash.h|json-c/linkhash.h|g' libgrive/src/protocol/Json.cc")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release \
                          -DCMAKE_EXE_LINKER_FLAGS=-ljson-c \
                          -DCMAKE_INSTALL_PREFIX=/usr ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "README")