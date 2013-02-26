#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

libdir = "/usr/lib/hevea"
bindir = "/usr/bin"

def build():
    pisitools.dosed("Makefile", "^PREFIX=/usr/local$", "PREFIX=%s" % get.defaultprefixDIR())
    pisitools.dosed("mylib.ml", "LIBDIR", libdir)
    autotools.make("BINDIR=%s LIBDIR=%s" % \
                    (get.installDIR() + bindir, \
                     get.installDIR() + libdir))

def install():
    pisitools.dodir(libdir)
    pisitools.dodir(bindir)
    autotools.rawInstall("BINDIR=%s LIBDIR=%s" % \
                          (get.installDIR() + bindir, \
                           get.installDIR() + libdir))

    pisitools.dodoc("README", "CHANGES", "LICENSE")
