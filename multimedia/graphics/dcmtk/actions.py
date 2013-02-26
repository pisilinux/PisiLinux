#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.export("CXXFLAGS", "%s -lcrypto -lpthread -lssh -lz" % get.CXXFLAGS())
    #shelltools.export("CFLAGS", get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -lcrypto -lssh -ljpeg -lz -lpthread" % get.LDFLAGS())
    shelltools.unlink("dcmjpls/libcharls")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_RPATH=OFF \
                          -DBUILD_SHARED_LIBS=ON \
                          -DDCMTK_WITH_OPENSSL=ON \
                          -DDCMTK_WITH_PNG=ON \
                          -DDCMTK_WITH_PRIVATE_TAGS=ON \
                          -DDCMTK_WITH_TIFF=ON \
                          -DDCMTK_WITH_XML=ON \
                          -DDCMTK_WITH_CHARLS=ON \
                          -DDCMTK_WITH_ZLIB=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("/usr/etc/*" ,"/etc")
    pisitools.removeDir("/usr/etc")