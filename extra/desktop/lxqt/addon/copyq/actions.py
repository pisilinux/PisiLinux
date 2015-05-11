# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DWITH_WEBKIT=0 \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DWITH_QT5=TRUE \
                          -DQT_QMAKE_EXECUTABLE=/usr/bin/qmake", sourceDir="..")

def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
