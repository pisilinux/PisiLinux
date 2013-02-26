#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    pythonmodules.compile()
    shelltools.chmod("examples/*", 0644)

def install():
    pythonmodules.install()

    pisitools.insinto(examples, "examples/*") 
    pisitools.insinto("/usr/share/pixmaps", "windows/icons/veusz.png")
    pisitools.insinto("usr/share/applications", "veusz.desktop")

    pisitools.dohtml("Documents/*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "VERSION", "Documents/*.txt", "Documents/*.pdf")
