#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.cxxflags.add("-fpermissive")
    shelltools.system("find -type f -name '*.moc.cpp' -exec rm -rf {} \;")
    shelltools.system("find -type f -name 'add.so' -exec rm -rf {} \;")
    shelltools.system("echo -e libs/libMatC/CJitFuncClang.hpp")
    shelltools.system("echo -e libs/libMatC/CJitFuncClang.cpp")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DUSE_LLVM=OFF \
                          -DFORCE_BUNDLED_UMFPACK=ON \
                          -DFFI_INCLUDE_DIR=/usr/lib/libffi-'pacman -Q libffi | cut -f2 -d\ |cut -f1 -d-'/include/ \
                          -DPYTHON_EXECUTABLE=/usr/bin/python2.7")

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())
    
    pisitools.remove("/usr/bin/blas.ini")