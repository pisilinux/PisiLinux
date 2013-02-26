#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


shelltools.export("HOME", "%s" % get.workDIR())
# WorkDir = ""
# NoStrip = "/"

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--prefix=/usr \
                         --with-json=system \
                         --enable-introspection \
                         --disable-static \
                         --enable-shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s INSTALL="install -p -c"' % get.installDIR())

    pisitools.dodoc("ChangeLog*", "COPYING", "README*", "NEWS")

