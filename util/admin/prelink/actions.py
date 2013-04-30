#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

def install():
    autotools.install()

    pisitools.dodir("/var/lib/prelink")
    pisitools.dodir("/var/log/prelink")
    pisitools.dodir("/etc/prelink.conf.d")

    pisitools.dodoc("ChangeLog", "README", "TODO", "THANKS", "AUTHORS", "COPYING", "NEWS")

