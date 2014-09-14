#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def fixPermissions():
    import os
    for root, dirs, files in os.walk("%s/opt" % get.installDIR()):
        for d in dirs:
            shelltools.system("/bin/chmod 0755 %s/%s" % (root, d))
        for f in files:
            shelltools.system("/bin/chmod 0644 %s/%s" % (root, f))

def install():
    pisitools.dodir("/opt/eclipse")

    pisitools.insinto("/opt/eclipse", "plugins")
    pisitools.insinto("/opt/eclipse", "features")

    # Fix file permissions (#7932)
    fixPermissions()
