#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/config.h", "/\* #define HAVE_DBUS \*/", "#define HAVE_DBUS")

    for f in ("dnsmasq.conf.example", "man/dnsmasq.8", "man/es/dnsmasq.8", "src/config.h"):
        pisitools.dosed(f, "/var/lib/misc", "/var/lib/dnsmasq")



def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())
    pisitools.insinto("/etc/dbus-1/system.d", "dbus/dnsmasq.conf", "dnsmasq.conf")

    # Install python binding
    pisitools.insinto("/usr/lib/%s/site-packages" % get.curPYTHON(), "dnsmasq.py")

    pisitools.dodir("/var/lib/dnsmasq")

    pisitools.dodoc("CHANGELOG", "COPYING", "COPYING-v3", "FAQ")
    pisitools.dohtml("doc.html", "setup.html")
