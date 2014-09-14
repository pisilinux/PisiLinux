#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

def install():
    #pisitools.insinto("/usr/share/applications/", "sofa.desktop")
    pisitools.insinto("/usr/share/sofastats/", "./sofa_main/*")
    #pisitools.insinto("/usr/share/sofastats/", "usr/share/java/e-takip/etakip.sh")
    pisitools.insinto("/usr/bin/", "./sofa_main/start.py")
    pisitools.dosym("/usr/share/sofastats/start.py", "/usr/bin/sofastats")
    #pisitools.insinto("/usr/share/pixmaps/", "sofa.png")