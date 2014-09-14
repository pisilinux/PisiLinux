#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile("build_ext -i")

def install():
    pythonmodules.install()

    pisitools.insinto("/usr/share/python-pysfml", "examples/*")

    shelltools.chmod("%s/usr/share/python-pysfml/*" % get.installDIR(), 0644)

    # pisitools.remove("/usr/share/python-pysfml/*.pyc")
    # pisitools.remove("/usr/share/python-pysfml/pong/*.pyc")
    # pisitools.remove("/usr/share/python-pysfml/shader/*.pyc")
