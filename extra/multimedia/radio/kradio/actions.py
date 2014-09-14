#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "KDE4_INCLUDE_DIR", "KDE4_INCLUDES")
    pisitools.dosed("CMakeLists.txt", "share\/doc\/kradio4", "share/doc/kradio")
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
