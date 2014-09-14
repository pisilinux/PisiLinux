#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools

WorkDir="musique"

def setup():
    #pisitools.dosed("musique.desktop", "=minitunes",  "=musique")
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.insinto("/usr/share/pixmaps/musique.png",  "images/app.png")
    pisitools.dodoc("CHANGES",  "COPYING",  "TODO")
