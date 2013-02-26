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

def build():
    autotools.make("CC=%s CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))
    #autotools.make("CC=%s CFLAGS=\"%s\" convert" % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dosed("man/Makefile", "^prefix \?= .*$", "prefix = /usr/share")
    autotools.rawInstall("bindir=/sbin DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/bin", "bcp", "btrfs-bcp")
    pisitools.insinto("/usr/bin", "show-blocks", "btrfs-show-blocks")

    pisitools.dosym("btrfsck", "/sbin/fsck.btrfs")

    pisitools.dodoc("COPYING")
