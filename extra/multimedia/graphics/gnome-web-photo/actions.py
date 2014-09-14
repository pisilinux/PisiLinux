#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --with-gtk=2.0 \
                         --disable-schemas-install")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Rename to avoid possible conflict with nautilus_thumbnailers
    pisitools.rename("/etc/gconf/schemas/thumbnailer.schemas", "gnome-web-thumbnail.schemas")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
