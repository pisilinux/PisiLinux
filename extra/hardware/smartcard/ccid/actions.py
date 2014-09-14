#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-twinserial \
                         --enable-serialconfdir=/etc/reader.conf.d \
                         --sysconfdir=/etc \
                         --disable-static \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/etc/", "src/Info.plist", "libccid_Info.plist")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
