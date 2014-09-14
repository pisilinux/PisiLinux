#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "lazarus"
NoStrip = [
        "/usr/lib/lazarus/components",
        "/usr/lib/lazarus/converter",
        "/usr/lib/lazarus/debugger",
        "/usr/lib/lazarus/designer",
        "/usr/lib/lazarus/examples",
        "/usr/lib/lazarus/ide",
        "/usr/lib/lazarus/ideintf",
        "/usr/lib/lazarus/lcl",
        "/usr/lib/lazarus/languages",
        "/usr/lib/lazarus/units"
        ]

def build():
    autotools.make("LCL_PLATFORM=qt bigide tools -j1")

def install():
    pisitools.insinto("/usr/lib", ".", "lazarus")

    pisitools.dosym("../lib/lazarus/lazarus", "/usr/bin/lazarus")
    pisitools.dosym("../lib/lazarus/lazbuild", "/usr/bin/lazbuild")
    pisitools.dosym("../../lib/lazarus/images/ide_icon48x48.png", "/usr/share/pixmaps/lazarus.png")

    pisitools.dodoc("*.txt")
