#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file `http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("rm -rf CMakeCache.txt")
    shelltools.cd("..")
    shelltools.makedirs("cmake-make")
    shelltools.cd("cmake-make") 
    shelltools.system("cmake ../blender-2.69 \
                      -DCMAKE_INSTALL_PREFIX=/usr \
                      -DCMAKE_BUILD_TYPE=Release \
                      -DCMAKE_SKIP_RPATH=ON \
                      -DWITH_JACK=ON \
                      -DWITH_IMAGE_OPENEXR=ON \
                      -DWITH_FFTW3=ON\
                      -DWITH_PLAYER=ON \
                      -DWITH_CODEC_FFMPEG=ON \
                      -DWITH_INSTALL_PORTABLE=OFF \
                      -DWITH_GAMEENGINE=ON \
                      -DWITH_PYTHON_INSTALL=OFF \
                      -DWITH_CODEC_SNDFILE=ON ")

def build():
    shelltools.cd("../cmake-make")
    cmaketools.make()

def install():
    shelltools.cd("../cmake-make/")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/blender", "/usr/bin", "blender-bin")

