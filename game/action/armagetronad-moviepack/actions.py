#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
