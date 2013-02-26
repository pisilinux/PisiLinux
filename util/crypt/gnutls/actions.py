#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("AUTOPOINT", "true")

    options = "--disable-static \
               --disable-rpath \
               --disable-dependency-tracking \
               --enable-guile \
               --with-lzo \
               --with-zlib \
               --with-libgcrypt \
               --with-included-libcfg"

    if get.buildTYPE() == "emul32":
        options += " --disable-hardware-acceleration"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
