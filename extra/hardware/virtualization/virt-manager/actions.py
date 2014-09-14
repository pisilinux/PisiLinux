#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
     pythonmodules.configure()
     pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("COPYING", "NEWS", "README*", "PKG-INFO")
