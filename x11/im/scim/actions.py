#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    shelltools.system("intltoolize --force")
    autotools.configure("--with-x \
                         --disable-static \
                         --enable-ld-version-script \
                         --x-includes=/usr/include/X11 \
                         --x-libraries=/usr/lib") # \
                         #--disable-panel-gtk \
                         #--disable-setup-ui")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Remove scim-setup related stuff
    pisitools.removeDir("/usr/share/pixmaps")
    pisitools.removeDir("/usr/share/applications")
    pisitools.removeDir("/usr/share/control-center-2.0")

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "TODO", "THANKS")
