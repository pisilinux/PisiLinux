#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.domove("/usr/bin/pyzord", "/usr/sbin")
    #pisitools.dohtml("docs/usage.html")
    pisitools.dodoc("COPYING", "README.txt", "NEWS")
