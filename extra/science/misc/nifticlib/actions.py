#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_SKIP_RPATH:BOOL=ON \
                          -DUSE_FSL_CODE:BOOL=OFF \
                          -DCMAKE_SHARED_LINKER_FLAGS=-Wl,--as-needed \
                          -DCMAKE_EXE_LINKER_FLAGS=-Wl,--as-needed ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("README", "LICENSE", "Updates.txt")

    shelltools.cd("docs")
    shelltools.system("doxygen Doxy_nifti.txt")

    pisitools.dohtml("html/*")
