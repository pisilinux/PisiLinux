#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install("--prefix=/usr")

    pisitools.dodoc("COPYING", "CHANGELOG", "AUTHORS", "README", "PKG-INFO")

    pisitools.remove("/usr/share/pytraffic/COPYING")
