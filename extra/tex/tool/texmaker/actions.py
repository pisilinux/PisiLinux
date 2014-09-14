#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.remove("/usr/share/texmaker/AUTHORS")
    pisitools.remove("/usr/share/texmaker/CHANGELOG.txt")
    pisitools.remove("/usr/share/texmaker/COPYING")

    pisitools.dodoc("utilities/AUTHORS", "utilities/COPYING", "utilities/CHANGELOG.txt")
