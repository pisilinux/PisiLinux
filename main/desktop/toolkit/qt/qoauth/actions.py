#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-src" % get.srcDIR()

def setup():
    #shelltools.system("qmake-qt4  PREFIX=%s" % get.qtDIR())
    qt4.configure()

def build():
    qt4.make()
    #autotools.make()
    pisitools.dosed("lib/libqoauth.prl", "^QMAKE_PRL_BUILD_DIR.*", "")

def install():
    qt4.install()
    #autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "LICENSE", "README")
