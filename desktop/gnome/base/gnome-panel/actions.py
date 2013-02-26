#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("LDFLAGS", "%s -lm -lgmodule-2.0 -lX11 -lcairo -lgdk-x11-2.0" % get.LDFLAGS())
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --disable-scrollkeeper \
                         --enable-bonobo \
                         --enable-introspection")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
