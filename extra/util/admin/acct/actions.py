#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-ivf")
    autotools.configure("--prefix=/usr \
                         --sbindir=/sbin \
                         --enable-linux-multiformat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/log/account")

    pisitools.remove("/usr/bin/last")
    pisitools.remove("/usr/share/man/man1/last.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "TODO", "COPYING", "NEWS", "README")
