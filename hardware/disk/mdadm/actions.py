#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def builddiet():
    autotools.make("clean")
    shelltools.export("CC", "diet %s %s %s %s -DHAVE_STDINT_H -Os -static" % (get.CC(), get.CFLAGS(), get.CXXFLAGS(), get.LDFLAGS()))
    autotools.make("mdadm.static")
    autotools.make("mdassemble.static")

    pisitools.insinto("/sbin", "mdadm.static")
    pisitools.insinto("/sbin", "mdassemble.static")

def build():
    # fix build with gcc-4.9.0
    pisitools.dosed("Makefile", "(Wall) -Werror", "\\1")
    # Not sure about MDASSEMBLE_AUTO=1. Need to investigate.
    autotools.make("SYSCONFDIR=/%s MDASSEMBLE_AUTO=1 mdassemble mdadm mdmon" % get.confDIR())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove the udev file as its shipped with udev package
    pisitools.remove("/lib/udev/rules.d/*")

    # Install config file
    pisitools.insinto("/etc", "mdadm.conf-example", "mdadm.conf")

    builddiet()

    pisitools.dodoc("TODO", "ChangeLog", "COPYING", "mdadm.conf-example", "misc/*")

