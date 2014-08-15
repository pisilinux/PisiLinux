#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS", "-Os")
    shelltools.system("sed 's|-O0|-Os|g' -i \"%s/efivar/Make.defaults\" || true" % get.workDIR())
    shelltools.system("sed 's|-rpath=$(TOPDIR)/src/|-rpath=$(libdir)|g' -i \"%s/efivar/src/test/Makefile\" || true" % get.workDIR())
    autotools.make("V=1 -j1")

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
