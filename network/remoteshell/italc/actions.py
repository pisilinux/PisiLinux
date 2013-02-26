#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    #autotools.autoreconf("-vfi")
    cmaketools.configure("--with-linux \
                         --with-x \
                         --enable-shared=yes \
                         --enable-static=no")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/italc")
    
    pisitools.domove("/usr/lib64/libItalcCore.so", "usr/lib/")

    pisitools.removeDir("/usr/lib64")
    #pisitools.removeDir("/usr/share/icons")
    #pisitools.removeDir("/usr/share/italc")

    pisitools.insinto("/usr/share/pixmaps", "ima/data/italc.png", "ica.png")
    pisitools.insinto("/usr/share/pixmaps", "ima/resources/fullscreen_demo.png", "italc.png")

    pisitools.dodoc("AUTHORS", "README", "TODO", "ChangeLog", "COPYING")
