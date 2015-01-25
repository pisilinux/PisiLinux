#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-print-profiles \
                         --disable-examples \
                         --disable-static \
                         --disable-rpath \
                         --disable-silent-rules \
                         --enable-polkit \
                         --enable-systemd-login=no \
                         --with-daemon-user=colord \
                         --with-systemdsystemunitdir=no \
                         --enable-introspection \
                         --enable-vala ")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO", "README.md")
