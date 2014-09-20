#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

def setup():
    kde4.configure("-DWITH_PulseAudio=ON \
                    -DCMAKE_SKIP_RPATH=ON \
                    -DWITH_QNtrack=OFF \
                    -DKDE4_ENABLE_FPIE=ON \
                    -DWITH_NepomukCore=OFF \
                    -DKDERUNTIME_BUILD_NEPOMUK=OFF \
                    -Wno-dev ")

def build():
    kde4.make()

def install():
    kde4.install()

    #remove index.theme file of hicolor icon theme, correct source for the file is the hicolor icon theme package itself
    pisitools.remove("/usr/share/icons/hicolor/index.theme")
    
    pisitools.dosym("/usr/lib/kde4/libexec/kdesud", "/usr/bin/kdesud")
