#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    # The gconf schema file gets installed in the wrong location so we move it
    pisitools.dodir("/etc/gconf/schemas")
    pisitools.domove("/usr/share/gconf/schemas/*", "/etc/gconf/schemas")
    os.removedirs("%s/usr/share/gconf/schemas" % get.installDIR())
