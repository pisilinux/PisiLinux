#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-20011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("CFLAGS","%s -fPIC -fno-strict-aliasing" % get.CFLAGS())

    autotools.autoreconf("-fi")
    autotools.configure("--without-regex \
                         --enable-shared \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "BUGS", "README","ChangeLog", "DEVINFO")
