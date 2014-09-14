#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    autotools.configure()

def build():
    autotools.make("V=1")
    shelltools.system("./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/dbus-1/interfaces", "org.freedesktop.RealtimeKit1.xml")

    pisitools.dodoc("README", "GPL", "LICENSE", "rtkit.c", "rtkit.h")
