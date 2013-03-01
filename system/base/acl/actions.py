#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPTIMIZER", get.CFLAGS())
    shelltools.export("DEBUG", "-DNDEBUG")

    autotools.rawConfigure("--libdir=/lib \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib \
                            --bindir=/bin")
def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install install-lib install-dev" % get.installDIR())

    pisitools.remove("/lib/*.a")

    shelltools.chmod("%s/lib/libacl.so.*.*.*" % get.installDIR(), 0755)

    pisitools.dodoc("README")
