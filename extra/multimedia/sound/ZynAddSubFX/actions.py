#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DOutputModule=jack -DGuiModule=fltk", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dodoc("*.txt", "COPYING", "ChangeLog")

    shelltools.cd("build")
    cmaketools.install()
