#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "README.txt")
