#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

datadir = "/usr/share/tremulous"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("base/server.cfg", "set sv_hostname.*", 'set sv_hostname "Tremulous Server on PisiLinux"')
    fixperms("base")

def install():
    pisitools.dodir(datadir)
    shelltools.copytree("base", "%s/%s/" % (get.installDIR(), datadir))
    shelltools.copy("gpp/*", "%s/usr/share/tremulous/base" % get.installDIR())
    for f in ["CC", "ChangeLog", "COPYING", "manual.pdf"]:
        pisitools.dodoc(f)

