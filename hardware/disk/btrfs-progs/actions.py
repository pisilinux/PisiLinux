#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    # Fix install prefix
    pisitools.dosed("Makefile", "^(prefix \?= \/usr)\/local", r"\1")

    autotools.make("V=1 CC=%s CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))
    autotools.make("V=1 CC=%s CFLAGS=\"%s\" btrfs-select-super" % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dosed("man/Makefile", "^prefix \?= .*$", "prefix = /usr/share")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.a")

    pisitools.insinto("/usr/bin", "bcp", "btrfs-bcp")
    pisitools.insinto("/usr/bin", "show-blocks", "btrfs-show-blocks")
    pisitools.insinto("/usr/bin", "btrfs-select-super")

    pisitools.dosym("btrfsck", "/usr/bin/fsck.btrfs")

    pisitools.dodoc("COPYING")
