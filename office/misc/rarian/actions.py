#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--sysconfdir=/etc \
                         --localstatedir=/var \
                         --disable-static \
                         --disable-skdb-update \
                         --enable-scrollkeeper-compat \
                         --enable-omf-read")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/var")
    pisitools.remove("/usr/bin/rarian-example")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "MAINTAINERS")
