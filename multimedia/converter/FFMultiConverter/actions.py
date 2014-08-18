#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile(pyVer = "3")

def install():
    pythonmodules.install(pyVer = "3")

    pisitools.dodoc("ChangeLog", "COPYING", "README*")
