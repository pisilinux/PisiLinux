#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='tuxtype_w_fonts-%s' % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/applications", "tuxtype.desktop")
    pisitools.insinto("/usr/share/pixmaps", "icon.png", "tuxtype.png")
    pisitools.dodir("/var/lib/tuxtype")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/AUTHORS", "doc/ChangeLog", "doc/TODO", "COPYING", "README", "doc/en/howtotheme.html")
