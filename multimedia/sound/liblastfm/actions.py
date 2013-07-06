#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DBUILD_TESTS=OFF \
                          -DCMAKE_INSTALL_LIBDIR=/usr/lib", sourceDir = "..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    # Docs
    pisitools.dodoc("COPYING","README*")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
