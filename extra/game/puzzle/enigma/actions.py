#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    for i in ["NEWS", "ChangeLog"]:
        shelltools.touch(i)
        
    #enet paket çakışması için silindi.
    #shelltools.unlinkDir("%s/enigma-1.21/lib-src/enet" % get.workDIR())
    autotools.configure("--disable-dependency-tracking \
                         --enable-optimize \
                         --enable-nls")
    shelltools.system("sed -i 's/root\.games/root.root/' Makefile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # we will use our desktop file
    pisitools.remove("/usr/share/applications/enigma.desktop")
    
    #enet ile çakışma yaşadığından dolayı. 
    pisitools.removeDir("/usr/include/enet/")

    pisitools.dodoc("ACKNOWLEDGEMENTS", "AUTHORS", "CHANGES", "README", "doc/HACKING")
    pisitools.dohtml("doc/*")
    pisitools.doman("doc/enigma.6")
