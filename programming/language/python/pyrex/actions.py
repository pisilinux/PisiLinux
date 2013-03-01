#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "Pyrex-%s" % get.srcVERSION()

def install():
    pythonmodules.install()

    pisitools.dodoc("CHANGES.txt", "README.txt", "USAGE.txt")
    pisitools.dohtml("Doc/*")
