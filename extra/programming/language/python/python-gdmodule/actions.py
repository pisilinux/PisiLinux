#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def build():
    shelltools.move("Setup.py","setup.py")

def install():
    pythonmodules.install()

    pisitools.dohtml("*.html")
    pisitools.dodoc("PKG-INFO", "README")
