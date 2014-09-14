#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--disable-static")
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON -DCMAKE_SKIP_RPATH=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dolib("build/*.so")
    pisitools.dobin("scripts/gtest-config")
    pisitools.insinto("/usr/include/gtest", "include/gtest/*.h")
    pisitools.insinto("/usr/include/gtest/internal", "include/gtest/internal/*.h")
    pisitools.insinto("/usr/share/gtest/src", "fused-src/gtest/*")
    pisitools.insinto("/usr/share/gtest", "CMakeLists.txt")
    pisitools.insinto("/usr/share/gtest/cmake", "cmake/*")
    pisitools.insinto("/usr/share/aclocal", "m4/gtest.m4")
    pisitools.dodoc("CHANGES", "CONTRIBUTORS", "LICENSE", "README")

