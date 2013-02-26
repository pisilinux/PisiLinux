#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libedit-20120601-3.0"

def setup():
    autotools.configure("--disable-static \
                         --enable-widec \
                         --disable-dependency-tracking \
                         --enable-fast-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "THANKS")
    pisitools.remove("/usr/lib/libedit.la")
