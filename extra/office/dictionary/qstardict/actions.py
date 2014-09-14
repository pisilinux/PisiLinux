#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

def setup():
    shelltools.system("qmake")

    shelltools.cd("kdeplasma")
    kde4.configure()

def build():
    autotools.make("CXX=%s" % get.CXX())

    shelltools.cd("kdeplasma")
    kde4.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())

    shelltools.cd("kdeplasma")
    kde4.install()
    shelltools.cd("..")

    pisitools.insinto("/usr/share/pixmaps", "qstardict/pixmaps/qstardict.png")
    pisitools.removeDir("/usr/share/doc/qstardict")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS")
