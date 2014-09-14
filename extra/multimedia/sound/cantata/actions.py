#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

def setup():
    #shelltools.system("svn up")
    cmaketools.configure("-DENABLE_KDE=OFF \
                          -DENABLE_CDPARANOIA=OFF \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("AUTHORS", "LICENSE", "ChangeLog", "TODO", "INSTALL", "README")
    
    pisitools.insinto("/usr/share/pixmaps/", "streams/icons/stream.png", "cantata.png")