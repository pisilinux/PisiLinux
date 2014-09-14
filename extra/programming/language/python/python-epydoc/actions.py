#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

def setup():
    shelltools.chmod("doc/*", 0644)

def install():
    pythonmodules.install()

    pisitools.dohtml("doc/*")
    pisitools.doman("man/*")
    pisitools.dodoc("LICENSE.txt", "README.txt")
