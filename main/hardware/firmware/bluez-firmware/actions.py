#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--libdir=/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/lib/firmware", "bfusb/*.frm")

    pisitools.remove("/lib/firmware/BCM-LEGAL.txt")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING", "NEWS", "broadcom/BCM-LEGAL.txt")
