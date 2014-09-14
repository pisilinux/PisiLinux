#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #autotools.autoreconf("-vif")
    autotools.configure("--disable-splash")

    # Remove zaz.pot so that make will create pot and catalog files
    #shelltools.unlink("po/zaz.pot")
    
    # Inject -lvorbis into the Makefile
    shelltools.system('sed -i -e "/^LIBS\s*=*/s|$| -lvorbis|" Makefile src/Makefile')

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/doc/zaz/INSTALL")
    
    pisitools.dosed("%s/usr/share/applications/zaz.desktop" % get.installDIR(), "Icon=zaz", "Icon=/usr/share/pixmaps/zaz.png")
