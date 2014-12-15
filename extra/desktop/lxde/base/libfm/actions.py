#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --enable-debug \
                         --enable-udisks \
                         --enable-demo")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/libfm-extra.so")
    pisitools.remove("/usr/lib/libfm-extra.so.4.0.3")
    pisitools.remove("/usr/lib/libfm-extra.so.4")
    pisitools.remove("/usr/include/libfm-1.0/fm-version.h")
    pisitools.remove("/usr/include/libfm-1.0/fm-extra.h")
    pisitools.remove("/usr/lib/pkgconfig/libfm-extra.pc")
    pisitools.remove("/usr/include/libfm-1.0/fm-xml-file.h")
    pisitools.dodoc("AUTHORS", "COPYING")

