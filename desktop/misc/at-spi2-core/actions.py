#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

libexec = "/tmp" if get.buildTYPE() == "emul32" else "/usr/libexec/at-spi2"

def setup():
    autotools.configure("--disable-static \
                         --disable-xevie \
                         --libexecdir=%s\
                         --with-dbus-daemondir=/usr/bin \
                        " % libexec)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.removeDir("/etc")
    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/tmp")
        return

    pisitools.dodoc("AUTHORS", "COPYING", "README", "NEWS")