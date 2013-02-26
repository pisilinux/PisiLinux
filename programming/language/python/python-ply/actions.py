#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ply-" + get.srcVERSION()

def build():
    pythonmodules.compile()
    pythonmodules.compile(pyVer = "3")

def install():
    pythonmodules.install()
    pythonmodules.install(pyVer = "3")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "TODO")
    shelltools.copy("%s/usr/share/doc/python-ply/*" % get.installDIR(), "%s/usr/share/doc/python3-ply" % get.installDIR())
