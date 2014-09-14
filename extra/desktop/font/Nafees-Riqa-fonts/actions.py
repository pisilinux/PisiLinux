#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/fonts/nafees", "Nafees Riqa v1.0.ttf", "Nafees_Riqa.ttf")
    shelltools.chmod("%s/usr/share/fonts/nafees/*" % get.installDIR(), 0644)
