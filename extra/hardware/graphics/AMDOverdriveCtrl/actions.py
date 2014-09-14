#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
   
    pisitools.domove("/usr/share/doc/packages/amdovdrvctrl/*", "%s/%s/" % (get.docDIR(), get.srcNAME()))
    
    pisitools.removeDir("/usr/share/menu/")
    pisitools.removeDir("/usr/share/doc/packages/")
    
    pisitools.domove("/usr/share/AMDOverdriveCtrl/images/icon.xpm", "/usr/share/pixmaps", "AMDOverdriveCtrl.xpm")
    pisitools.removeDir("/usr/share/AMDOverdriveCtrl/")