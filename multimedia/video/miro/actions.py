#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

shelltools.export("HOME", get.workDIR())

def build():
    shelltools.cd("linux")
    pythonmodules.compile()

def install():
    shelltools.cd("linux")
    pythonmodules.install()

    shelltools.cd("..")
    pisitools.dodoc("CREDITS", "LAYOUT", "README")
