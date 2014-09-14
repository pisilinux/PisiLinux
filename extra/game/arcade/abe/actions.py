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

datadir = "/usr/share/abe"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("-with-data-dir=%s" % datadir)

def build():
    autotools.make()

def install():
    pisitools.dodir(datadir)
    pisitools.dobin("src/abe")

    for d in ["images", "sounds", "maps"]:
        fixperms(d)
        shelltools.copytree(d, "%s/%s/" % (get.installDIR(), datadir))

    pisitools.dodoc("AUTHORS", "ChangeLog", "README*")

