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
    autotools.configure("--prefix=/usr \
			 --disable-static \
                         --enable-vala \
                         --enable-introspection")

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/var/pisi/libgusb-0.1.6-3/install/usr", "/")
    pisitools.removeDir("/var")


    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
