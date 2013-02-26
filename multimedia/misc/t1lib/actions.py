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

def setup():
    pisitools.dosed("doc/Makefile.in", "dvips", "#dvips")
    pisitools.dosed("xglyph/xglyph.c", "\./\(t1lib\.config\)", "/etc/t1lib/\1")

    autotools.configure("--datadir=/etc \
                         --with-x \
                         --enable-static=no")


def build():
    autotools.make("without_doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("Changes", "README*")
