#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "./"

def install():
    
    pisitools.insinto("/usr/share/icons", "pacifica-icon-theme-master/Pacifica")
    
    pisitools.dodoc("pacifica-icon-theme-master/CREDITS", "pacifica-icon-theme-master/README.md")
