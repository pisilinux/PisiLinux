#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./configure.tcl --nodepcheck --quiet --libdir=usr/lib/tcl8.6 --bindir=usr/bin --prefix=usr/lib --bintarget=/usr/share/tv-viewer")


def install():
    shelltools.system("./install.tcl")

    pisitools.insinto("/usr/bin", "usr/bin/*")    
    pisitools.insinto("/usr/lib/tcl8.6", "usr/lib/tcl8.6/*")
    pisitools.insinto("/usr/share/tv-viewer", "usr/lib/share/tv-viewer/*")
    pisitools.insinto("/usr/share/man/man1", "usr/lib/share/man/man1/*")
    pisitools.insinto("/usr/share/pixmaps", "usr/lib/share/pixmaps/*")
    pisitools.insinto("/usr/share/applications", "usr/lib/share/applications/*")   
    pisitools.insinto("/usr/share/doc", "usr/lib/doc/*")
