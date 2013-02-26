#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "foomatic-db-%s" % get.srcVERSION().split("_", 1)[1]
NoStrip = "/"

def setup():
    # For gutenprint printers, use gutenprint-ijs-simplified.5.2
    pisitools.dosed("db/source/printer/*.xml", ">gutenprint<", ">gutenprint-ijs-simplified.5.2<")

    autotools.configure()

    # Cleanup conflicts
    shelltools.cd("db/source")
    shelltools.system("../../cleanup-conflicts")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fix permissions
    for root, dirs, files in os.walk("%s/usr/share/foomatic/db" % get.installDIR()):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
