#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="coquillo-"+get.srcVERSION()

def setup():
    qt4.configure(projectfile="coquillo.pro", parameters="CONFIG+=release CONFIG-=debug PREFIX=/usr")

def build():
    qt4.make()

def install():
    qt4.install()
    
    pisitools.dodoc("CHANGES", "INSTALL", "LICENSE", "README")
