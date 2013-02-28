#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/gfxtheme/pardus"

def build():
    autotools.make('PRODUCT="Pardus 2011"')

def install():
    pisitools.insinto(datadir, "bootlogo.dir", "install")
    pisitools.insinto(datadir, "message.dir", "boot")

