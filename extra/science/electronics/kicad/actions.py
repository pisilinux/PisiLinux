#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools

def setup():
    pisitools.dosed("pcbnew/dialogs/dialog_fp_lib_table.cpp","wxRE_ADVANCED","wxRE_EXTENDED")
    pisitools.dosed("CMakeLists.txt", "-O2", "-O1")
    
    cmaketools.configure("-DKICAD_STABLE_VERSION=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DwxWidgets_CONFIG_EXECUTABLE='/usr/bin/wxconfig' \
                          -DwxWidgets_wxrc_EXECUTABLE='/usr/bin/wxrc'")
                          
    for i in ["library", "doc"]:
        shelltools.cd(i)
        cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")
        shelltools.cd("..")

def build():
    cmaketools.make()
    
    for i in ["library", "doc"]:
        shelltools.cd(i)
        cmaketools.make()
        shelltools.cd("..")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    for i in ["library", "doc"]:
        shelltools.cd(i)
        cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
        shelltools.cd("..")
        
    pisitools.dodoc("AUTHORS.txt", "CHANGELOG*", "COPYRIGHT.txt", "TODO.txt", "README.txt")
