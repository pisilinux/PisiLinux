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

WorkDir = "prelink"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def check():
    autotools.make("-C testsuite check-harder CC='gcc -Wl,--add-needed' CXX='g++ -Wl,--add-needed'")
    autotools.make("-C testsuite check-cycle CC='gcc -Wl,--add-needed' CXX='g++ -Wl,--add-needed'")

def install():
    autotools.install()

    pisitools.dodir("/var/lib/prelink")
    pisitools.dodir("/var/log/prelink")
    pisitools.dodir("/etc/prelink.conf.d")

    pisitools.dodoc("ChangeLog", "README", "TODO", "THANKS", "AUTHORS", "COPYING", "NEWS")

