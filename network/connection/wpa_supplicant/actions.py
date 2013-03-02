#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.cd("wpa_supplicant")

    #Enable syslog output
    cflags = get.CFLAGS() + " -DCONFIG_DEBUG_SYSLOG"
    shelltools.export("CFLAGS", cflags)

    autotools.make("V=1")
    autotools.make("eapol_test")

def install():
    shelltools.cd("wpa_supplicant")

    for bin in ["wpa_supplicant", "wpa_cli", "wpa_passphrase", "eapol_test"]:
        pisitools.dosbin(bin)

    # Install dbus files
    pisitools.insinto("/usr/share/dbus-1/system-services", "dbus/*.service")
    pisitools.insinto("/etc/dbus-1/system.d", "dbus/dbus-wpa_supplicant.conf", "wpa_supplicant.conf")

    pisitools.doman("doc/docbook/*.5")
    pisitools.doman("doc/docbook/*.8")
    pisitools.newdoc("wpa_supplicant.conf", "wpa_supplicant.conf.example")

    pisitools.dodoc("ChangeLog", "../COPYING", "eap_testing.txt", "../README", "todo.txt")