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
    autotools.configure("\
                         --disable-static \
                         --disable-update-mime \
                         --disable-schemas-compile \
                         --enable-introspection \
                         --with-dbus-services=/usr/share/dbus-1/services")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #remove files conflicted with gnome-keyring
    #pisitools.remove("/usr/share/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml")
    #pisitools.remove("/usr/share/GConf/gsettings/org.gnome.crypto.pgp.convert")

    pisitools.dodoc("AUTHORS", "ChangeLog","COPYING", "README", "NEWS")
