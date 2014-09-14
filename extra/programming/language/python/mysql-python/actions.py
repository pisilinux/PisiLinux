#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules

WorkDir = "MySQL-python-1.2.3"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
