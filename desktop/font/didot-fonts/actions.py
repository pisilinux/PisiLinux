#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="ttf-gfs-didot-classic-1.1"

def install():
    pisitools.insinto("/usr/share/fonts/didot","*.otf");
    pisitools.dodoc("*.txt");

