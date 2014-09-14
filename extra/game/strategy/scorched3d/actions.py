#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "scorched"
def setup():
    #autotools.aclocal()
    #autotools.automake("--foreign")
    #autotools.autoconf()
    autotools.configure("--prefix=/usr \
                         --datadir=/usr/share/scorched3d \
                         --disable-openaltest \
                         --with-wx-config=wx-config")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGELOG", "README")
