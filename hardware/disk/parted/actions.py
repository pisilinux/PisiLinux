#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # FIXME: device-mapper is not in system.base discuss it
    autotools.configure("--disable-device-mapper \
                         --disable-static \
                         --without-readline \
                         --enable-Werror=no")

def build():
    autotools.make('CFLAGS="%s" CXXFLAGS="%s" CC="%s" CXX="%s"' %
            (get.CFLAGS(), get.CXXFLAGS(), get.CC(), get.CXX()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.dodoc("doc/API", "doc/USER.jp", "doc/FAT")

    #pisitools.removeDir("/usr/bin")
