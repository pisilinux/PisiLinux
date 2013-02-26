#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # icons
    pisitools.removeDir("/usr/share/pixmaps")
    pisitools.insinto("/usr/share/icons/hicolor/32x32/apps/", "data/amoebax.png")
    pisitools.insinto("/usr/share/icons/hicolor/scalable/apps/", "data/amoebax.svg")

    # docs
    pisitools.removeDir("/usr/share/doc")
    pisitools.dodoc("AUTHORS", "COPYING*", "doc/manual.pdf", "THANKS", "TODO", "README")
