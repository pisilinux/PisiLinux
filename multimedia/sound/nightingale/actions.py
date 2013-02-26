#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nightingale-%s" % get.srcVERSION()

def build(): 
    shelltools.system("./build.sh \
                       -with-pthreads \
                       -enable-canvas \
                       -enable-system-cairo \
                       -enable-gio \
                       -with-system-zlib \
                       -enable-ffmpeg \
                       -prefix=/usr")
    
    
def install():
    shelltools.makedirs("%s/usr/share/" % get.installDIR())
    shelltools.copytree("compiled/dist", "%s/usr/share/nightingale" % get.installDIR())
    
    pisitools.insinto("/usr/share/pixmaps/", "app/branding/nightingale-512.png", "nightingale.png")
    pisitools.dosym("/usr/share/nightingale/nightingale-bin", "/usr/bin/nightingale")
    
    pisitools.dodoc("*.txt", "LICENSE", "README")
    
