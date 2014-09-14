#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"
WorkDir = "moviepack"
targetdir = "/usr/share/armagetronad/moviepack"

def install():
    pisitools.dodir(targetdir)
    shelltools.copy("*", "%s/%s" % (get.installDIR(), targetdir))
