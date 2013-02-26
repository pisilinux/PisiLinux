#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "qsvn-0.8.3"
NoStrip = ["/usr/share/pixmaps", "/usr/share/doc"]

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DBUILD_TESTS=OFF", sourceDir="../src")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")

    pisitools.dodoc("ChangeLog", "README")
