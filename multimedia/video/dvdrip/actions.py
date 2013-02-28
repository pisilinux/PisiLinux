#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.insinto("/usr/share/applications", "dvdrip.desktop")
    pisitools.insinto("/usr/share/pixmaps", "lib/Video/DVDRip/icon.xpm", "dvdrip.xpm")

    pisitools.dodoc("Changes*", "COPYRIGHT", "Credits", "README", "TODO")
