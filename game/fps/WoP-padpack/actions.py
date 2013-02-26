#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = "/"

def install():
    pisitools.insinto("/usr/share/WoP/wop", "wop_padpack.pk3")

    pisitools.dodoc("*.txt")
