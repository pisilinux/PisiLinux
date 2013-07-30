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
    shelltools.system("cmake ../blender-2.68 \
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
    cmaketools.make()

def install():
    shelltools.cd("../") 
    shelltools.cd("build_linux/")
    pisitools.insinto("/usr/bin/", "bin/blender","blender-bin")
    pisitools.insinto("/usr/bin/", "bin/blender-thumbnailer.py")
    pisitools.insinto("/usr/share/man/man1", "bin/blender.1")
    pisitools.insinto("/usr/share/doc/", "bin/*.txt")
    pisitools.insinto("/usr/share/doc/", "bin/*.html")
    pisitools.insinto("/usr/share/pixmaps/", "bin/blender.svg")
    pisitools.insinto("/usr/share/", "bin/2.68/datafiles/locale/")
    pisitools.insinto("/usr/share/blender/", "bin/2.68/scripts")
    
    shelltools.cd("../") 
    shelltools.cd("blender-2.68/release/")
    ## Install miscellaneous files
    pisitools.insinto("/usr/share/blender/", "scripts/*")
    
    pisitools.insinto("/usr/share/blender/", "datafiles/colormanagement/")

    ##Install icon files
    pisitools.insinto("/usr/share/icons/hicolor/", "freedesktop/icons/*")
