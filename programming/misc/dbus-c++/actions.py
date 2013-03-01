#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "dbus-c++"

def setup():
    pisitools.dosed("configure.ac", "-O3", "")
    shelltools.export("CPPFLAGS", get.CXXFLAGS())

    shelltools.system("./autogen.sh")
    autotools.configure("--disable-static \
                         --enable-glib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "COPYING")
