#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ufoai-%s-source" % get.srcVERSION()
datadir = "/usr/share/ufoai"
exefiles = ["ufo", "ufo2map", "ufoded"]

def setup():
    shelltools.export("CFLAGS", "%s -mmmx -msse" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -mmmx -msse" % get.CXXFLAGS())

    shelltools.makedirs("base")
    autotools.configure('--enable-release \
                         --enable-dedicated \
                         --enable-client \
                         --enable-ufo2map \
                         --localedir="%s/base/i18n" \
                         --disable-uforadiant \
                         --disable-paranoid \
                         --disable-profiling \
                         --disable-hardlinkedgame' % datadir)
                         #--bindir= \
                         #--datarootdir="datadir/base" \
                         #--datadir="datadir" \


def build():
    autotools.make()
    autotools.make("lang")

def install():
    pisitools.insinto(datadir, "base")

    for f in exefiles:
        pisitools.dobin(f)

    pisitools.dodoc("COPYING", "README")

