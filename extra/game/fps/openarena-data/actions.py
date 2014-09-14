#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

NoStrip = "/"
# 0.8.5 is a patch over 0.8.1
WorkDir = "openarena-0.8.8"
#WorkDir = "openarena-%s" % get.srcVERSION()

docs = ["CHANGES", "COPYING", "CREDITS", "LINUXNOTES", "README", "WENEED"]
datadir = "/usr/share/openarena"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    for data in ("missionpack", "baseoa"):
        fixperms(data)
        pisitools.insinto(datadir, data)

    for doc in docs:
        pisitools.dodoc(doc)
