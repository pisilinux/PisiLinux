#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
     shelltools.makedirs("build")
     
     shelltools.cd("build")
     cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                           -DPYLIB_INSTALL_DIR=lib/python2.7/site-packages \
                           -DUSE_EXTERNAL_TBB=ON \
                           -DUSE_OCIO= OFF \
                           -DOIIO_BUILD_TESTS=OFF", sourceDir="..")
     
def build():
    shelltools.cd("build")  
  
    cmaketools.make()

def install():
    shelltools.cd("build")
    
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR()) 
    #pisitools.insinto("/usr/bin", "dist/*/bin/*")
    #pisitools.insinto("/usr/include", "dist/*/include/*")
    #pisitools.insinto("/usr/lib", "dist/*/lib/*")
    #pisitools.insinto("/usr/lib", "dist/*/python/*")
    #pisitools.insinto("/usr/share/doc", "dist/*/doc*")
    
    #pisitools.dodoc("CREDITS", "LICENSE", "README.*")
