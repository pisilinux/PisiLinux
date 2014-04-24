#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DQTGSTREAMER_EXAMPLES=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("NEWS", "COPYING*", "README")