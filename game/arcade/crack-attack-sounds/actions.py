#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "data"

def install():
    pisitools.dodir("/usr/share/crack-attack")
    shelltools.copytree("sounds", "%s/usr/share/crack-attack/sounds" % get.installDIR())
