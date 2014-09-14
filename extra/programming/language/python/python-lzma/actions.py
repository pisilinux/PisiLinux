#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "pylzma-0.4.4"

def install():
    pythonmodules.install()

    pisitools.dodoc("LICENSE.txt", "readme.txt")
