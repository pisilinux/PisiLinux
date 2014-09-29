#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = get.srcNAME()

def build():
    shelltools.system('export CFLAGS="$CFLAGS -fPIC -fexceptions -fvisibility=hidden -DNO_LCMS"')
    shelltools.system('export CXXFLAGS="$CXXFLAGS -fPIC -fexceptions -fvisibility=hidden -DNO_LCMS"')
    shelltools.system('sed -i "1 i #include <cstring>" Source/OpenEXR/IlmImf/ImfAutoArray.h')
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          LIBDIR=/usr/lib" % get.installDIR())

    pisitools.dodoc("*.txt", "README.linux")
