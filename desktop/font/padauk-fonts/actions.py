#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.insinto("/usr/share/fonts/padauk/", "*.ttf")
    pisitools.dodoc("README","padauk.cfg")

