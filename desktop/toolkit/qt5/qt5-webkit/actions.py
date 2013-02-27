#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4
from pisi.actionsapi import qt4
from pisi.actionsapi import get

import os

WorkDir = "q"
shelltools.export("HOME", get.workDIR())

def setup():
    pass
 

def build():
    shelltools.system('./Tools/Scripts/build-webkit --qt --only-webkit --install-headers=/home/q/zagor/include \
		      --minimal --install-libs=/home/q/zagor/lib --no-webkit2 --cmakeargs="-DCMAKE_PREFIX_PATH=/usr"')

def install():
    autotools.install()