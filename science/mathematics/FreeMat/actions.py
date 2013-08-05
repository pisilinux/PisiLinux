#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #Remove pre-created compilation stuff.
    pisitools.unlink("CMakeCache.txt")
    pisitools.unlink("libs/lib*/*.moc.*")     
    pisitools.unlink("src/*.moc.*")
    cmaketools.configure('-DFFI_INCLUDE_DIR:PATH=/usr/lib/libffi-3.0.12/include \
                        -DCMAKE_BUILD_TYPE:STRING=Release \
                        -DBoost_DIR:PATH=/usr/lib \
                        -DFORCE_SYSTEM_LIBS:BOOL=ON \
                        -DCMAKE_INSTALL_PREFIX:PATH=/usr -L \
                        -DBUILD_SHARED_LIBS:BOOL=OFF \
                        -DUSE_LLVM=OFF \
                        -DUSE_ITK=OFF \
                        -DFORCE_BUNDLED_PCRE=OFF \
                        -DFORCE_BUNDLED_UMFPACK=OFF \
                        -DFORCE_BUNDLED_PORTAUDIO=OFF \
                        -DFORCE_BUNDLED_ZLIB=OFF \
                        -DFORCE_BUNDLED_AMD=OFF')

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps/", "images/freemat-2.xpm", "FreeMat.xpm")
    pisitools.remove("/usr/bin/blas.ini")