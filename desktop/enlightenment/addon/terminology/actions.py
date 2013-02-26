#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="terminology-%s" % get.srcVERSION()

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    shelltools.system("./autogen.sh")
    autotools.autoreconf("-vfi")
    autotools.rawConfigure("--libdir=/usr/lib \
                            --prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*")
