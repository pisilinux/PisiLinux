#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

params = "-DLIB_SUFFIX=32 \
          -DCMAKE_INSTALL_LIBDIR=lib32 \
          -DQT_LIBRARY_DIR=/usr/lib32 \
          -DQZeitgeist_DIR=/usr/lib32/cmake/QZeitgeist \
          -DQT_PLUGINS_DIR=/usr/lib32/qt4/plugins \
          -DQT_IMPORTS_DIR=/usr/lib32/qt4/imports" if get.buildTYPE() == "emul32" else ""

if get.buildTYPE() == "emul32": shelltools.export("CMAKE_LIBRARY_PATH", "/usr/lib32")

def setup():
    cmaketools.configure('-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=ON \
                          -DQT_QMAKE_EXECUTABLE=/usr/bin/qmake \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_SKIP_RPATH:BOOL=YES %s' % params)

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32": return

    #some applications like mediaplayer example of Qt needs this #11648
    pisitools.dosym("/usr/include/KDE/Phonon", "/usr/include/Phonon")
