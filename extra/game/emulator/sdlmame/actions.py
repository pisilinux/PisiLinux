#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

import os
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("unzip *.zip")
    shelltools.system("unzip mame.zip")
    shelltools.system("tar -zxvf extras.tar.gz")

def build():
    autotools.make("NOWERROR=1 OPTIMIZE=2")
    autotools.make("tools NOWERROR=1 OPTIMIZE=2")

def install():
    data_dir = "/usr/share/%s" % get.srcNAME()
    for b in [f for f in os.walk("./").next()[2] if os.access(f, os.X_OK)]:
        pisitools.insinto(data_dir, b)
    pisitools.insinto("%s/shader" % data_dir, "src/osd/sdl/shader/glsl*.*h")
    pisitools.insinto("/usr/share/man/man1", "src/osd/sdl/man/*.1*")
    pisitools.insinto("/usr/share/man/man6", "src/osd/sdl/man/*.6*")
    for d in ["artwork", "ctrlr", "src/osd/sdl/keymaps"]:
        pisitools.insinto("%s/%s" % (data_dir, d.split("/").pop()), "%s/*" % d)
        
    pisitools.dosym("/usr/share/sdlmame/mame64", "/usr/bin/sdlmame")    

    pisitools.dodoc("docs/*")
