#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
