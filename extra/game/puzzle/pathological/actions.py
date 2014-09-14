#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

NoStrip = "/"

datadir = "/usr/share/pathological"
dirs = ["circuits", "graphics", "music", "sounds"]

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)


def setup():
    shelltools.system("/bin/gunzip pathological.6.gz")
    shelltools.chmod("pathological.py", 0755)
    shelltools.chmod("pathological_scores", 0644)

    for d in dirs:
        fixperms(d)

def install():
    pisitools.insinto(datadir, "pathological.py")
    pisitools.insinto(datadir, "pathological_scores")

    for d in dirs:
        shelltools.copytree(d, "%s/%s/" % (get.installDIR(), datadir))

    pisitools.insinto("/usr/share/pixmaps/", "pathological.xpm")

    pisitools.dohtml("html/*")
    pisitools.doman("pathological.6")
    pisitools.dodoc("README", "TODO", "LICENSE")

