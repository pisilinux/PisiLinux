#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-nasm \
                         --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s" pkghtmldir="/%s/%s/html"' % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("API", "ChangeLog", "HACKING", "README*", "STYLEGUIDE", "TODO", "USAGE")
    pisitools.dohtml("misc/*", "Dll/*")
    pisitools.dobin("misc/mlame")
    
    pisitools.remove("/usr/lib/libmp3lame.so")
    pisitools.remove("/usr/lib/libmp3lame.so.0")
    
    
    
    pisitools.dosym("/usr/lib/libmp3lame.so.0.0.0", "/usr/lib/libmp3lame.so")
    pisitools.dosym("/usr/lib/libmp3lame.so.0.0.0", "/usr/lib/libmp3lame.so.0")