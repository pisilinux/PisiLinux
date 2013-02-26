# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def install():
    pythonmodules.install()
    
    pisitools.insinto("/usr/share/pixmaps/", "data/pixmap/cr64-app-kaptan.png", "kaptan.png")
    
