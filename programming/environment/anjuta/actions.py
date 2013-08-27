#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
shelltools.export("LC_ALL", "C")


def setup():
    autotools.configure("--disable-silent-rules \
                         --disable-static \
                         --enable-plugin-devhelp \
                         --enable-plugin-sourceview \
                         --enable-plugin-glade \
                         --enable-introspection \
                         --disable-scrollkeeper \
                         --enable-gtk-doc")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "FUTURE", "MAINTAINERS", "NEWS", "README", "ROADMAP", "THANKS", "TODO")