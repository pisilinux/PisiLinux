#!/usr/bin/python
# -*- coding: utf-8 -*-


from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    #thanks to s.dalgic
    shelltools.export("pardusCC", get.CC())
    shelltools.export("pardusCXX", get.CXX())
    shelltools.export("pardusCFLAGS", get.CXX())
    shelltools.export("pardusCPPFLAGS", get.CXXFLAGS())
    
    shelltools.cd("build/workspaces/")
    shelltools.system("./update-workspaces.sh \
                        --with-system-mozjs185 \
                        --with-system-enet \
                        JOBS=%s" % get.makeJOBS())

def build():
    shelltools.cd("build/workspaces/gcc")
    autotools.make("V=1 CONFIG=Release")

def install():
    pisitools.dodoc("LICENSE.txt","license_dbghelp.txt","license_gpl-2.0.txt","license_lgpl-2.1.txt","README.txt",)
    pisitools.insinto("/opt/0ad","binaries/*")
    pisitools.insinto("/usr/share/pixmaps/", "build/resources/0ad.png", "0ad.png")
    pisitools.insinto("/usr/share/applications/", "build/resources/0ad.desktop", "0ad.desktop")
    pisitools.insinto("/usr/share/applications/", "build/resources/0ad-editor.desktop", "0ad-editor.desktop")

