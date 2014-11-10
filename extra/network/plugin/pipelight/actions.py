#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("sed -i '39d' Makefile")
    shelltools.system("sed -i '1s| src/windows||g' Makefile")
    shelltools.system("sed -i '2 a\ CXXFLAGS        := -static-libgcc -static-libstdc++ $(CXXFLAGS)' src/windows/Makefile")
    shelltools.touch("configure.in")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr --wine-path=/usr/bin/wine --win32-static")
    shelltools.system("tar xfvz pluginloader-prebuilt-v0.2.3.tar.xz")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/usr/share/pipelight", "pluginloader.exe")
    
    shelltools.system("public-scripts/pipelight-plugin --destdir=/var/pisi/pipelight-0.2.3-1/install/ --create-mozilla-plugins ")
    
    pisitools.domove("/usr/lib/pipelight/libpipelight-silverlight5.1.so", "/usr/lib/browser-plugins")
    
    pisitools.dodoc("LICENSE")