#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure('-DBUILD_DEMOS=OFF \
                          -DINSTALL_STATIC=OFF \
                          -DCMAKE_C_FLAGS="%s -ffast-math -fPIC -DCHIPMUNK_FFI"' % get.CFLAGS())

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README.textile", "LICENSE.txt")
