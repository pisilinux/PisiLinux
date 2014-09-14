#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("srcbuild")
    shelltools.cd("srcbuild")
    cmaketools.configure(sourceDir="..")

def build():
    shelltools.cd("srcbuild")
    cmaketools.make()

def install():
    shelltools.cd("srcbuild")
    cmaketools.install()
    
    shelltools.cd("..")
    pisitools.dodoc("README.txt", "COPYING.txt", "REGISTER.txt")
