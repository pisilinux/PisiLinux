#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i -e 's/wx-config/wx-config-2.8/' configure")
    shelltools.export("WX_CONFIG", "/usr/bin/wx-config-2.8 ")
    autotools.configure("--disable-static \
                         --disable-debug \
                         --disable-dependency-tracking \
                          --with-wx-config=/usr/bin/wx-config-2.8 \
                         --with-wx-version=2.8")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "pkg/debian/pgadmin3.xpm")
