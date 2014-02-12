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
    #for i in ["mtools.texi"]:
    #    pisitools.dosed(i, "/usr/local/etc", "/etc")

    shelltools.export("INSTALL_PROGRAM", "install")
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/usr \
			             --sysconfdir=/etc/mtools \
                         --includedir=/usr/src/linux/include")

def build():
    autotools.make()
    pisitools.dosed("mtools.conf","SAMPLE FILE","#SAMPLE FILE")
def install():
    autotools.rawInstall('-j1 DESTDIR="%s"' % get.installDIR())
    

    pisitools.insinto("/etc/mtools","mtools.conf")
    
    pisitools.dodoc("COPYING", "README*", "Release.notes")
