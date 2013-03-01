#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pyosd-%s" % get.srcVERSION()
mods = "%s/%s/modules" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.chmod("modules/*", 0644)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
    pisitools.dohtml("pyosd.html")
    pisitools.insinto(mods, "modules/*")

