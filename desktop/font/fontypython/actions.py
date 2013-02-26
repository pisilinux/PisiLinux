#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.doman("fontypython.1")
    pisitools.dodoc("README","COPYING","CHANGELOG")
