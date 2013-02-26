#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Cython-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dohtml("Doc/*.html")
    pisitools.dodoc("COPYING.txt", "LICENSE.txt", "README.txt", "ToDo.txt", "USAGE.txt")
