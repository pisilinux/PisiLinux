#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/applications", "desktop/dreamchess.desktop")
    pisitools.insinto("/usr/share/pixmaps", "desktop/dreamchess.png")

    pisitools.dodoc("ChangeLog", "README", "NEWS", "COPYING", "AUTHORS")
