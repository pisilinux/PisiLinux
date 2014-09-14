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
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE \
                          -DCLUCENE_LIBRARY_DIR=/usr/include \
                          -DENABLE_FAM=OFF \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DENABLE_POLLING=ON \
                          -DENABLE_FFMPEG=OFF \
                          -DENABLE_INOTIFY=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
