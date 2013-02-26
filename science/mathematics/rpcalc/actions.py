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

WorkDir = "rpCalc"

def install():
    pythonmodules.run("install.py -p %s/usr/" % get.installDIR())

    pisitools.dosed("%s/usr/bin/rpcalc" % get.installDIR(), "/var/pisi/%s/install" % get.srcTAG())
    pisitools.dosed("%s/usr/lib/rpcalc/rpcalc.py" % get.installDIR(), "/var/pisi/%s/install" % get.srcTAG())
