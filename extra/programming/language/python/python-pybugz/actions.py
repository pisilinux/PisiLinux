#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

#WorkDir = "pybugz-0.9.2_20121116"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
