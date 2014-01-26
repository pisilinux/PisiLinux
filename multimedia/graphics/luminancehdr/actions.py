#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "/lib", "/usr/lib")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")
def build():
    cmaketools.make("LIBS=%s" % get.LDFLAGS())

def install():
    cmaketools.install("libdir=%s/usr/lib" % get.installDIR())
    pisitools.dodoc("AUTHORS","BUGS","LICENSE","TODO")
