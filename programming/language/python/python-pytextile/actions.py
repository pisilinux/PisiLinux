#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir="textile-%s" % get.srcVERSION()

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()
