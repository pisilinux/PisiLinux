#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build-cmake")
    shelltools.cd("build-cmake")
    cmaketools.configure("-DWL_PORTABLE=true \
                          -DWL_INSTALL_PREFIX=/usr \
                          -DWL_INSTALL_BINDIR=bin \
                          -DWL_INSTALL_DATADIR=share/widelands \
                          -DWL_INSTALL_LOCALEDIR=/usr/share/widelands/locale \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release", sourceDir="..")

def build():
    shelltools.cd("build-cmake")
    cmaketools.make()

def install():
    pisitools.dodoc("COPYING", "CREDITS", "ChangeLog")

    shelltools.cd("build-cmake")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

