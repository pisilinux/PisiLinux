#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-threads")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/lib/udev/rules.d")
    pisitools.domove("/etc/udev/rules.d/45-hpdjconsole.rules", "/lib/udev/rules.d/")
    pisitools.removeDir("/etc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
