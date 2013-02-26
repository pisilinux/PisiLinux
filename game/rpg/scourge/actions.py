#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcNAME()

def setup():
    autotools.configure("--disable-rpath \
                         --disable-dependency-tracking \
                         --with-data-dir=/usr/share/scourge")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "assets/scourge.desktop")
    pisitools.insinto("/usr/share/pixmaps", "assets/scourge.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
