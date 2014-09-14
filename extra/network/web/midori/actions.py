#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

shelltools.export("LC_ALL", "C")
WorkDir = "."

def setup():
    autotools.rawConfigure("--prefix=/usr")
    cmaketools.configure("-DUSE_GTK2=OFF -DUSE_GTK3=1 -DCMAKE_SKIP_RPATH=ON -DCMAKE_SKIP_INSTALL_RPATH=ON")
    
    pisitools.dosed("CMakeCache.txt", "lib64", "lib")
    pisitools.dosed(".", "lib64", "lib", filePattern="cmake_install.cmake")

def build():
    cmaketools.make()


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

