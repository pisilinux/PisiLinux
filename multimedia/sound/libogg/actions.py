#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    cflags = get.CFLAGS()
    options = "--disable-static"
    pisitools.dosed("doc/Makefile.in", "^docdir = .*$", "docdir = $(datadir)/doc/$(PACKAGE)")
    pisitools.dosed("doc/libogg/Makefile.in", "^docdir = .*$", "docdir = $(datadir)/doc/$(PACKAGE)/ogg")

    if get.buildTYPE() == "emul32":
        cflags += " -m32"
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", cflags)

    pisitools.dosed("configure", "-O20", cflags)
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "CHANGES", "COPYING", "README")
