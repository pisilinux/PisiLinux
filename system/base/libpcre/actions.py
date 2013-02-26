#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

def setup():
    options = "--enable-jit \
               --enable-pcretest-libreadline \
               --enable-pcre8 \
               --enable-pcre16 \
               --enable-utf8 \
               --enable-unicode-properties \
               --enable-cpp \
               --docdir=/%s/%s \
               --disable-static" % (get.docDIR(), get.srcNAME())

    if get.buildTYPE() == "emul32":
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

    libtools.libtoolize("--copy --force")
    autotools.autoreconf("-vif")
    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
