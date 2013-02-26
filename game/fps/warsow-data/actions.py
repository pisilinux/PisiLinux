#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# workdir changes all the time
#WorkDir = "./"
WorkDir = "warsow_0.61_unified"
NoStrip = "/"

import os

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("basewsw")

def install():
    pisitools.insinto("/usr/share/warsow", "basewsw")

    shelltools.move("docs/license.txt", "docs/license-data.txt")
    pisitools.dodoc("docs/*", destDir="warsow")
