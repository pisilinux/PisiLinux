#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("examples/CMakeLists.txt", "\$\{DATA_DIR\}\/examples", "/usr/share/plplot")
    pisitools.dosed("examples/*/CMakeLists.txt", "\$\{DATA_DIR\}\/examples", "/usr/share/plplot")
    pisitools.dosed("cmake/modules/instdirs.cmake", "_VERSION", "")
    pisitools.dosed("cmake/modules/instdirs.cmake", "doc\/\$\{PACKAGE\}", "doc/plplot/${PF}")
    #pisitools.dosed("cmake/modules/tcl-related.cmake", "3.4 3.3 3.2 3", "4.0.0 3.4 3.3 3.2 3")

    cmaketools.configure("-DUSE_RPATH=OFF     \
                          -DENABLE_ada=OFF    \
                          -DHAVE_ADA_2007=OFF \
                          -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
                          -DENABLE_d=OFF      \
                          -DENABLE_octave=OFF \
                          -DENABLE_pyqt4=OFF \
                          -DENABLE_java=ON \
                          -DJAR_DIR=/usr/share/plplot/java \
                          -DENABLE_lua=ON \
                          -DENABLE_tcl=ON \
                          -DENABLE_qt=ON \
                          -DENABLE_wxwidgets=ON \
                          -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wxconfig \
                          -DFREETYPE_INCLUDE_DIR=/usr/include/freetype2 \
                          -DTEST_DYNDRIVERS=OFF \
                         ")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.doman("doc/*.1")
