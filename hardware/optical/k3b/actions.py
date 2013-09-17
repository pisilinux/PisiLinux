#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure("-DK3B_BUILD_K3BSETUP:BOOL=OFF \
                    -DK3B_ENABLE_HAL_SUPPORT:BOOL=OFF")

def build():
    kde4.make()

def install():
    kde4.install()
