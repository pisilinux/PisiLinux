#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/gfxtheme/pisi"

def build():
    autotools.make('PRODUCT="Pisi"')

def install():
    pisitools.insinto(datadir, "bootlogo.dir", "install")
    pisitools.insinto(datadir, "message.dir", "boot")

