#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("examples/CMakeLists.txt", "\$\{DATA_DIR\}\/examples", "/usr/share/plplot")
    pisitools.dosed("examples/*/CMakeLists.txt", "\$\{DATA_DIR\}\/examples", "/usr/share/plplot")
    pisitools.dosed("cmake/modules/instdirs.cmake", "\$\{VERSION\}", "")
    pisitools.dosed("cmake/modules/instdirs.cmake", "doc\/\$\{PACKAGE\}", "doc/plplot/${PF}")

    cmaketools.configure("-DUSE_RPATH=OFF     \
                          -DENABLE_ada=OFF    \
                          -DHAVE_ADA_2007=OFF \
                          -DENABLE_d=OFF      \
                          -DENABLE_octave=OFF \
                          -DENABLE_java=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.doman("doc/*.1")
