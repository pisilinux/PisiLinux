#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from os import system

WorkDir = "."

def install():
    pisitools.insinto("/usr/bin", "update-ms-fonts")
    pisitools.insinto("/usr/share/fonts/msttcorefonts", "cabfiles.sha256sums")
    pisitools.insinto("/usr/share/fonts/msttcorefonts", "uninstall")
