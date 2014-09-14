#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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

