#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("CMakeLists.txt", "LIB_SUFFIX 64", deleteLine="True")

    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DPYTHON_EXECUTABLE=/usr/bin/python2.7 \
                          -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                          -DPYTHON_LIBRARY=/usr/lib/python2.7 \
                          -DCMAKE_SKIP_BUILD_RPATH=ON \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DEXAMPLES=OFF -DFTDI_EEPROM=OFF")


def build():
    autotools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #Remove python examples
    pisitools.removeDir("/usr/share/libftdi")
    
    # Their source can be useful though
    pisitools.dodoc("examples/*.c", destDir="%s/examples" % get.srcNAME())

    # Install udev rule
    pisitools.insinto("/lib/udev/rules.d", "packages/99-libftdi.rules")

    pisitools.doman("doc/man/man3/*.3")

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "README")
