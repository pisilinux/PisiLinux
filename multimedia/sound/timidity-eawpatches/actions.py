#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
from os.path import join

NoStrip = "/"
WorkDir = "./"

def setup():
    pisitools.dosed("eawpats/linuxconfig/timidity.cfg", "dir /home/user/eawpats/", "dir /usr/share/timidity/eawpatches")

    for root, dirs, files in os.walk("eawpats"):
        for name in dirs:
            shelltools.chmod(join(root, name), 0755)
        for name in files:
            shelltools.chmod(join(root, name), 0644)

    shelltools.copy("eawpats/linuxconfig/timidity.cfg", "eawpats/timidity.cfg")

def install():
    pisitools.dodir("/usr/share/timidity")
    shelltools.copytree("eawpats", "%s/usr/share/timidity/eawpatches" % get.installDIR())

    pisitools.removeDir("/usr/share/timidity/eawpatches/linuxconfig")
    pisitools.removeDir("/usr/share/timidity/eawpatches/winconfig")

