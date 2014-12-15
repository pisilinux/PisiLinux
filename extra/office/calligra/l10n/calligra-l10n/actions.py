#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4
from pisi.actionsapi import get

WorkDir = "."
SkipFiles = [".pc", "filelist", "patches", "pisiBuildState"]

def setup():
    for klasorler in shelltools.ls("."):
        if klasorler in SkipFiles:
            continue
        shelltools.cd(klasorler)
        kde4.configure()
        shelltools.cd("../")    

def build():
    for klasorler in shelltools.ls("."):
        if klasorler in SkipFiles:
            continue
        shelltools.cd(klasorler)
        kde4.make()
        shelltools.cd("../")    

def install():
    for klasorler in shelltools.ls("."):
        if klasorler in SkipFiles:
            continue
        shelltools.cd(klasorler)
        kde4.install("DESTDIR=%s" % get.installDIR())
        shelltools.cd("../")
    
