#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mudur"

def install():
    shelltools.system("./setup.py install %s" % get.installDIR())

    pisitools.dodir("/etc/mudur/services/enabled")
    pisitools.dodir("/etc/mudur/services/disabled")
    pisitools.dodir("/etc/mudur/services/conditional")
