#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

Base = "%s/usr/lib/ocaml" % get.installDIR()

def setup():
    shelltools.system('echo "COPTS= -c -O %s" >> Makefile.config' % get.CFLAGS())

def build():
    autotools.make("-j1 lib")

def install():
    shelltools.makedirs("%s/usr/bin" % get.installDIR())
    shelltools.makedirs("%s/stublibs" % Base)

    autotools.install("BINDIR=%s/usr/bin INSTALLDIR=%s/lablGL DLLDIR=%s/stublibs" % (get.installDIR(), Base, Base))

    pisitools.remove("/usr/lib/ocaml/lablGL/*.a")
    pisitools.dodoc("CHANGES", "COPYRIGHT", "README")

    pisitools.insinto("%s/lablgl/examples/Togl" % get.docDIR(), "Togl/examples")
    pisitools.insinto("%s/lablgl/examples/LablGlut" % get.docDIR(), "LablGlut/examples")
