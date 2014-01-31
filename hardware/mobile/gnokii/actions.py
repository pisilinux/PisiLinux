#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    #autotools.autoreconf("-fi")

    autotools.configure("--enable-static=no \
                         --enable-security \
                         --enable-bluetooth \
                         --enable-libpcsclite \
                         --enable-postgres \
                         --enable-irda \
                         --enable-smsd \
                         --enable-libical \
                         --with-x \
                         --with-bluetooth=/usr/lib")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.insinto("/etc", "Docs/sample/gnokiirc")

    # install headers
    pisitools.insinto("/usr/include", "include/gnokii.h")
    pisitools.insinto("/usr/include/gnokii", "include/gnokii/*")

    pisitools.removeDir("/usr/share/doc/gnokii")

    # install docs
    pisitools.doman("Docs/man/*.1*", "Docs/man/*.8")
    pisitools.dodoc("Docs/README*", "Docs/CREDITS", "Docs/FAQ")

    # we will use our own desktop file and icon
    #pisitools.remove("/usr/share/applications/xgnokii.desktop")
