#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

import os

WorkDir = "pygame-%srelease" % get.srcVERSION()
docdir = "%s/%s" % (get.docDIR(), get.srcNAME())
pyversion = get.curPYTHON().replace("python", "")
arch = get.ARCH().replace("-", "_")

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    for d in ["src", "lib", "docs", "examples"]:
        fixperms(d)

    pythonmodules.run("config.py -auto")

def build():
    pythonmodules.compile()
    shelltools.copy("lib/pygame_icon.bmp", "build/lib.linux-%s-%s/pygame/" % (arch, pyversion))

def install():
    pythonmodules.install()

    pisitools.insinto(docdir, "docs", "html")
    pisitools.insinto(docdir, "examples")
