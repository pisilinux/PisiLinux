#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("usr/lib64/libOpenThreads.so.2.3.0", "/usr/lib/")
    pisitools.domove("usr/lib64/libOpenThreads.so.11", "/usr/lib/")
    pisitools.domove("usr/lib64/libOpenThreads.so", "/usr/lib/")
    
    pisitools.removeDir("usr/lib64")

    pisitools.dodoc("AUTHORS.txt", "ChangeLog", "TODO.txt", "README.txt")
