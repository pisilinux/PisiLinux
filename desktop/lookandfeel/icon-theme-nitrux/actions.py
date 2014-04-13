#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

WorkDir = "."

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("%s/NITRUX-KDE/apps/scalable/linuxdcpp.sv*" % get.workDIR())

def install():
    pisitools.insinto("/usr/share/icons", "NITRUX-KDE")

