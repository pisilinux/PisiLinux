#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

# Source tarball is made by hand, to make it
# wget http://downloads.sourceforge.net/tremulous/tremulous-1.1.0.zip
# unzip tremulous-1.1.0.zip
# wget http://prdownloads.sourceforge.net/tremulous/tremulous-gpp1.zip
# unzip tremulous-gpp1.zip
# cp -R tremulous/gpp/* tremulous/base/
# mkdir tremulous-data-1.2.0_beta1
# cp -R tremulous/base tremulous-data-1.2.0_beta1
# cp -R tremulous/C* tremulous-data-1.2.0_beta1
# cp -R tremulous/manual.pdf tremulous-data-1.2.0_beta1
# tar -czf tremulous-data-1.2.0_beta1.tar.gz tremulous-data-1.2.0_beta1


#WorkDir = "tremulous"
datadir = "/usr/share/tremulous"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    pisitools.dosed("base/server.cfg", "set sv_hostname.*", 'set sv_hostname "Tremulous Server on Pardus"')
    fixperms("base")

def install():
    pisitools.dodir(datadir)
    shelltools.copytree("base", "%s/%s/" % (get.installDIR(), datadir))

    for f in ["CC", "ChangeLog", "COPYING", "manual.pdf"]:
        pisitools.dodoc(f)

