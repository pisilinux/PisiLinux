#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Os")
    autotools.make("all")

def install():
    pisitools.dosed("Makefile","BINDIR := /usr/sbin","BINDIR := %s/usr/sbin" % get.installDIR())
    shelltools.makedirs("%s/usr/sbin" % get.installDIR())
    shelltools.makedirs("%s/usr/lib" % get.installDIR())
    shelltools.makedirs("%s/usr/share/man" % get.installDIR())
    shelltools.makedirs("%s/usr/include" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/lib", "src/lib/*.o")
    pisitools.insinto("/usr/share/man", "src/man/*")
    pisitools.insinto("/usr/include", "src/include/*.h")
