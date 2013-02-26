#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

# Workdir changes all the time
WorkDir = "glest-source-%s" % get.srcVERSION()
# WorkDir = "./"

def fixperms(target):
    for root, dirs, files in os.walk(target):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def dos2unix(target):
    for root, dirs, files in os.walk(target):
        for name in files:
            pisitools.dosed(os.path.join(root, name), "\r")

def setup():
    for d in shelltools.ls("./"):
        if shelltools.isDirectory(d):
            fixperms(d)

    dos2unix("mk")

    shelltools.chmod("autogen.sh", 0755)
    shelltools.system("./autogen.sh")

    shelltools.unlink("glest_map_editor")
    dos2unix("../")

    #pisitools.dosed("Jamrules", "^COMPILER_CFLAGS_optimize \+=.*", "COMPILER_CFLAGS_optimize += %s ;" % get.CFLAGS())
    #pisitools.dosed("Jamrules", "^COMPILER_C\+\+FLAGS_optimize \+=.*", "COMPILER_C++FLAGS_optimize += %s ;" % get.CXXFLAGS())
    #pisitools.dosed("Jamrules", "^COMPILER_LFLAGS_optimize \+=.*", "COMPILER_LFLAGS_optimize += %s ;" % get.LDFLAGS())
    #pisitools.dosed("Jamrules", "-O3 -DNDEBUG", "-DNDEBUG")

    pisitools.dosed("glest_game/main/main.cpp", "PARDUS_DATADIR", "/usr/share/glest/")

    autotools.configure("--with-ogg \
                         --with-vorbis \
                         --with-wx-config=disabled_wx \
                         --with-x")

def build():
    shelltools.system("jam -dx -q")

def install():
    # Trying out a filepath patch
    # pisitools.doexe("glest", "/usr/share/glest/lib")
    pisitools.dobin("glest")

