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
    pisitools.dosed("configure.ac", "(SCIM_HAS_CLUTTER=)yes", "\\1no")
    autotools.autoreconf("-vfi")
    shelltools.system("intltoolize --force")
    autotools.configure("\
                         --with-x \
                         --disable-static \
                         --enable-ld-version-script \
                         --x-includes=/usr/include/X11 \
                         --x-libraries=/usr/lib \
                         --disable-clutter-immodule \
                        ") 
                         #--disable-panel-gtk \
                         #--disable-setup-ui")
                       
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove scim-setup related stuff
    pisitools.removeDir("/usr/share/pixmaps")
    pisitools.removeDir("/usr/share/applications")
    pisitools.removeDir("/usr/share/control-center-2.0")

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "TODO", "THANKS")
