#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--prefix=/usr \
			 --sysconfdir=/etc \
			 --libexecdir=/usr/lib/gnome-keyring")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/glib-2.0/schemas/org.gnome.crypto.pgp.gschema.xml")
    pisitools.remove("/usr/share/GConf/gsettings/org.gnome.crypto.pgp.convert")

    pisitools.dodoc("AUTHORS", "ChangeLog","COPYING", "README", "NEWS")
