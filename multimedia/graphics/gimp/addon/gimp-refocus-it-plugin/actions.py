#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.rawConfigure("--bindir=/usr/lib/gimp/2.0/plug-ins")
    #pisitools.dosed("src/Makefile", "--sort-common", "--sort-common, -lm")
    #pisitools.dosed("lib/Makefile", "--sort-common", "--sort-common, -lm")
    #pisitools.dosed("gtk-doc/Makefile", "--sort-common", "--sort-common, -lm")
    #pisitools.dosed("doc/Makefile", "--sort-common", "--sort-common, -lm")
    #pisitools.dosed("Makefile", "--sort-common", "--sort-common, -lm")
    #shelltools.system("gcc -shared -Wl,-soname, -L/usr/lib/atlas -llapack -lm")
    shelltools.export("LDFLAGS", "%s -L/lib64/libm.so.6" % get.LDFLAGS())
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
