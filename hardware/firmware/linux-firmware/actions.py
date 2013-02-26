#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "linux-firmware-20121212"

def setup():
    # Remove source files
    shelltools.unlink("usbdux/*dux")
    shelltools.unlink("*/*.asm")

    # These + a lot of other firmware are shipped within alsa-firmware
    for fw in ("ess", "korg", "sb16", "yamaha"):
        shelltools.unlinkDir(fw)

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/lib/firmware", "mix/*")

    # Remove installed and LIC* files from /lib/firmware
    pisitools.remove("/lib/firmware/GPL-3")
    pisitools.remove("/lib/firmware/LICENCE*")
    pisitools.remove("/lib/firmware/LICENSE*")
    pisitools.remove("/lib/firmware/configure")
    pisitools.remove("/lib/firmware/Makefile")
    pisitools.remove("/lib/firmware/ipw2200-bss.fw")
    pisitools.remove("/lib/firmware/ipw2200-ibss.fw")
    pisitools.remove("/lib/firmware/ipw2200-sniffer.fw")
    pisitools.removeDir("/lib/firmware/mix")

    # Install LICENSE files
    pisitools.dodoc("WHENCE", "LICENCE.*", "LICENSE.*", "GPL-3")
