#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

lines = ["_V = ",
         "_E = echo",
         "INSTALL_DIR=%s/usr/share/openttd/data/opengfx" % get.installDIR(),
         "DOCDIR=%s/usr/share/doc/%s" % (get.installDIR(), get.srcNAME())]

def setup():
    for f in shelltools.ls("docs"):
        if f.endswith("ptxt"): shelltools.sym(f, "docs/%s" % f.replace("ptxt", "txt"))

    with open("Makefile.local", 'w') as file:
        for line in lines:
            file.write("%s\n" % line)

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/openttd/data/opengfx", "*.grf")
    pisitools.insinto("/usr/share/openttd/data/opengfx", "*.obg")
    
    pisitools.dodoc("docs/changelog.txt", "docs/readme.ptxt", "docs/license.txt", "docs/readme.txt")
