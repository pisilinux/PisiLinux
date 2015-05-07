#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    qt5.configure()

def build():
    qt5.make()
    qt5.make("docs")

def install():
    qt5.install("INSTALL_ROOT=%s" % get.installDIR())
    qt5.install("install_docs")
