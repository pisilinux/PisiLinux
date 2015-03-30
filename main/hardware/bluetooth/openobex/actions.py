#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("--disable-static \
                         --enable-bluetooth \
                         --enable-irda \
                         -DCMAKE_INSTALL_LIBDIR=lib \
                         --enable-usb")
    
   # pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share/man")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "ChangeLog")
