#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "projectM-%s-Source" % get.srcVERSION()
shelltools.export("CXXFLAGS", "%s -lGL" % get.CXXFLAGS())

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dosym("libprojectM.so.2.0.1", "/usr/lib/libprojectM.so.2")

    pisitools.remove("/usr/share/projectM/presets/Geiss & Sperl - Feedback (projectM idle HDR mix).prjm")

    #pisitools.dodoc("ChangeLog")
