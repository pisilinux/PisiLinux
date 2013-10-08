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
                         --disable-systemd-login \
                         --with-daemon-user=colord \
                         --enable-introspection \
                         --enable-vala \
                         --enable-sane")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO", "README.md")
