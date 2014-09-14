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
    pythonmodules.install("--optimize=1")

    pisitools.removeDir("/usr/lib/python2.7/site-packages/M2Crypto-*")

    pisitools.dodoc("PKG-INFO" , "README")
