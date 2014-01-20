#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

monoristol = "/usr/share/doc/monobristol/"
WorkDir = "."

def setup():
    shelltools.cd("bristol-0.60.11")
    autotools.configure("--prefix=/usr \
                         --disable-version-check \
                         --enable-jack-default-audio \
                         --enable-jack-default-midi ")
    
    shelltools.cd("..")    
    shelltools.cd("monobristol-0.60.3")
    autotools.configure()
    shelltools.cd("..")

def build():
    shelltools.cd("bristol-0.60.11")
    autotools.make()
    shelltools.cd("..")
    shelltools.cd("monobristol-0.60.3")
    autotools.make()
    shelltools.cd("..")

def install():    
    shelltools.cd("bristol-0.60.11")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")
    shelltools.cd("..")
    shelltools.cd("monobristol-0.60.3")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/applications/", "monoBristol.desktop")
    pisitools.insinto("/usr/share/pixmaps/", "monobristol.png")
    
    for files in ["AUTHORS", "COPYING", "README"]:
        pisitools.insinto(monoristol, files)
    
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps/", "monobristol.png")
   
    

    

