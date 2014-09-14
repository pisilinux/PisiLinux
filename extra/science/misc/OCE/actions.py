#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    
    shelltools.cd("build")
    cmaketools.configure("-DOCE_INSTALL_PREFIX=/usr  \
                          -DOCE_WITH_FREEIMAGE=ON \
                          -DOCE_WITH_GL2PS=ON", sourceDir="..")            
      
def build():
    shelltools.cd("build")
    autotools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "LICENSE*.*", "NEWS", "README.*")