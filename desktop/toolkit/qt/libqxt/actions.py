#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import qt4

WorkDir = 'libqxt-libqxt-dadc327c2a6a'

def setup():
    autotools.rawConfigure("-prefix /usr \
                            -libdir /usr/lib \
                            -headerdir /usr/include \
                            -qmake-bin /usr/bin/qmake")

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.removeDir("/usr/doc")
