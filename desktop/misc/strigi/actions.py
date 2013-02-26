#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pkgconfig
from pisi.actionsapi import get

def setup():
    #FIXME: External libstreams workaround
    if not pkgconfig.libraryExists("libstreams"):
        raise "libstreams pkgconfig file not found!"

    libstreams_version = pkgconfig.getLibraryVersion("libstreams")

    MAJOR = libstreams_version.split(".")[0]
    MINOR = libstreams_version.split(".")[1]
    PATCH = libstreams_version.split(".")[2]
    STRING = libstreams_version

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_INSTALL_RPATH_USE_LINK_PATH=FALSE \
                          -DCLUCENE_LIBRARY_DIR=/usr/include \
                          -DENABLE_FAM=ON \
                          -DENABLE_POLLING=ON \
                          -DENABLE_INOTIFY=ON \
                          -DSTRIGI_VERSION_MAJOR=%s \
                          -DSTRIGI_VERSION_MINOR=%s \
                          -DSTRIGI_VERSION_PATCH=%s \
                          -DSTRIGI_VERSION_STRING=%s \
                          -DLIBSTREAMS_VERSION=%s \
                          " % (MAJOR, MINOR, PATCH, STRING, STRING), sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("../")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
