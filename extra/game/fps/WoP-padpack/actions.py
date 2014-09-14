#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = "/"

def install():
    pisitools.insinto("/usr/share/WoP/wop", "wop_padpack.pk3")

    pisitools.dodoc("*.txt")
