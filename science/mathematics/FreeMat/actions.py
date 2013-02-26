#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "FreeMat-4.1-Source"

def setup():
    #Remove pre-created compilation stuff.
    pisitools.unlink("CMakeCache.txt")
    pisitools.unlink("libs/lib*/*.moc.*")     
    pisitools.unlink("src/*.moc.*")
    cmaketools.configure('-DFFI_INCLUDE_DIR:PATH=/usr/lib/libffi-3.0.9/include -DCMAKE_BUILD_TYPE:STRING=Release -D Boost_DIR:PATH=/usr/lib \
                      -D FORCE_SYSTEM_LIBS:BOOL=ON -D CMAKE_INSTALL_PREFIX:PATH=/usr -L')

def build():
    #shelltools.system('./tools/buildtool /usr native-freemat') bu script güncel değil yoksa buda kullanılabilirdi.
    shelltools.system('make -j8')

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps/", "images/freemat-2.xpm", "FreeMat.xpm")
    #pisitools.remove("/usr/bin/blas.ini")
