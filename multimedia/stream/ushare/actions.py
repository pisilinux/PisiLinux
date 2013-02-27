#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --sysconfdir=/etc \
                            --enable-dlna")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/etc/init.d")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO")
