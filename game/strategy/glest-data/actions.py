#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "./"
datasource = "glest_game"

def fixperms(Dir):
    for root, dirs, files in os.walk(Dir):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            # espa? langfiles have strange encodings and borks
            if name.endswith(".lng") and "espa" in name:
                shelltools.unlink(os.path.join(root, name))
            else:
                shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms(datasource)

def install():
    pisitools.insinto("/usr/share/glest/", "%s/*" % datasource)

    # Buggy character coding
    #pisitools.remove("/usr/share/glest/data/lang/espa*")
    #pisitools.remove("/usr/share/glest/scenarios/storming/storming_espa*")

    # We will use the ini file from the source code
    # pisitools.remove("/usr/share/glest/glest.ini")
