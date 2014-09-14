#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()
    
def install():
    pythonmodules.install()
    for lc in shelltools.ls("po/*.po"): pisitools.domo(lc,  lc[3:-3],  'quod-libet.mo')
    
   
    
   