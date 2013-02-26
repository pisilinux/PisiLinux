#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

ARCH = get.ARCH().replace("686", "386")

buildDir = "build/release-linux-%s" % ARCH
dataDir = "/usr/share/smokinguns"

def build():
    autotools.make("DEFAULT_BASEDIR=%s copyfiles" % dataDir)

def install():
    pisitools.insinto("/usr/bin", "%s/smokinguns.%s" % (buildDir, ARCH), "smokinguns")
    pisitools.insinto("/usr/bin", "%s/smokinguns_dedicated.%s" % (buildDir, ARCH), "smokinguns-server")

    pisitools.dodoc("BUGS", "ChangeLog", "TODO", "README", "*.txt")
