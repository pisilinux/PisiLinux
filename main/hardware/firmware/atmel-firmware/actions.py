#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("%s -o atmel_fwl atmel_fwl.c" % get.CC())

def install():
    pisitools.insinto("/lib/firmware/", "images/*.bin")
    pisitools.insinto("/lib/firmware/", "images.usb/*.bin")

    pisitools.insinto("/etc/pcmcia", "atmel.conf")

    pisitools.insinto("/usr/sbin", "atmel_fwl")
    pisitools.insinto("/usr/sbin", "atmel_fwl.pl")

    pisitools.doman("atmel_fwl.8")

    pisitools.dodoc("README", "COPYING", "VERSION")
