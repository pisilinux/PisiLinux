#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-Wcpp -DCMAKE_BUILD_TYPE=Release \
                          -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wxconfig \
                          -DENABLE_LAPACK=yes \
                          -DVIGRA_INCLUDE_DIR=/usr/include")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "TODO")
