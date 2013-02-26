#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "./"
NoStrip = "/"

f = "NOGRAVITY.RMX"
d = "/usr/share/nogravity"

def setup():
    shelltools.chmod(f, 0644)

def install():
    pisitools.dodir(d)
    pisitools.insinto(d, f)

