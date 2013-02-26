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
    pisitools.dosed("timidity.cfg", "dir /nethome/sak95/shom/lib/timidity/", "dir /usr/share/timidity/shompatches/")
    pisitools.dosed("sfx.cfg", "^source ", "source shompatches/")
    pisitools.dosed("timidity.cfg", "^source ", "source shompatches/")

    for root, dirs, files in os.walk("inst"):
        for name in dirs:
            shelltools.chmod(join(root, name), 0755)
        for name in files:
            shelltools.chmod(join(root, name), 0644)

    shelltools.chmod("*.cfg", 0644)

def install():
    pisitools.dodir("/usr/share/timidity/shompatches")
    pisitools.insinto("/usr/share/timidity/shompatches", "*.cfg")
    pisitools.insinto("/usr/share/timidity/shompatches", "inst")
