#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools

WorkDir = "freecad-0.13.1830"

def setup():
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    cmaketools.configure("-DOCC_INCLUDE_DIR:PATH=/usr/include/oce \
                          -DCMAKE_INSTALL_DATADIR=/usr/share/freecad \
                          -DCOIN3D_DOC_PATH=/usr/share/doc/coin \
                          -DFREECAD_USE_EXTERNAL_PIVY:BOOL=ON \
                          -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python", sourceDir = "..")
    #for build plugin   
    shelltools.cd("../src/Tools/plugins/widget")
    shelltools.system("qmake plugin.pro")

def build():
    shelltools.cd("%s/%s/build" % (get.workDIR(),WorkDir))
    cmaketools.make()
    
    #build plugin
    shelltools.cd("../src/Tools/plugins/widget")
    autotools.make()         

def install():
    libtools.libtoolize()
    
    shelltools.cd("%s/%s/build" % (get.workDIR(),WorkDir))
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #install plugin
    pisitools.insinto("/usr/lib/qt4/plugins/designer/", "../src/Tools/plugins/widget/*.so")
    
    shelltools.cd("..")
    pisitools.dodoc("README","ChangeLog.*", "copying.*")

    