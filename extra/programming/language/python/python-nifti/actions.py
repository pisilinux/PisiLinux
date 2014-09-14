#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("setup.py", "'--Wl,--no-undefined'")
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHOR", "COPYING", "Changelog", "PKG-INFO", "TODO")
    pisitools.doman("man/*")