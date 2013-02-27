#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = get.srcNAME()
shelltools.export("HOME", get.workDIR())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          LIBDIR=/usr/lib" % get.installDIR())

    pisitools.dodoc("*.txt", "README.linux")
