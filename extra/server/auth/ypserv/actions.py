#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fpic" % get.CFLAGS())

def setup():
    autotools.configure("--enable-checkroot \
                         --enable-fqdn")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc", "etc/ypserv.conf")
    pisitools.insinto("/etc", "etc/netgroup")
    pisitools.insinto("/etc", "etc/netmasks")

    pisitools.insinto("/var/yp", "etc/securenets")
    pisitools.insinto("/var/yp", "Makefile")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
