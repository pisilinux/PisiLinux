#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "."

def build():
    autotools.make("LIB=/lib")

def install():
    autotools.rawInstall("DESTDIR=%s \
                          LIB=/lib \
                          bindir=/sbin \
                          syslibdir=/lib \
                          libmpathdir=/lib/multipath" % get.installDIR())

    pisitools.dodir("/etc/multipath")
    pisitools.removeDir("/etc/init.d")

    pisitools.dodoc("AUTHOR", "COPYING", "FAQ")
