#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    pisitools.dobin("gtviewer")

    pisitools.insinto("/usr/share/applications", "gtviewer.desktop")
    pisitools.insinto("/usr/share/info", "gtviewer.info")
    pisitools.insinto("/usr/share/pixmaps", "gtviewer_logo.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "gtviewer.html", "gtviewer.txt")
