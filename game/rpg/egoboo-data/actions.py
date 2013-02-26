#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"
WorkDir="egoboo-%s" % get.srcVERSION()

data = "/usr/share/egoboo"
docs = ["Changelog.txt", "license.txt", "controls.txt"]


def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def install():
    pisitools.dodir(data)

    for d in [ "basicdat", "modules"]:
        fixperms(d)
        pisitools.insinto(data, d)

    for f in docs:
        pisitools.dodoc(f, destDir="egoboo")

