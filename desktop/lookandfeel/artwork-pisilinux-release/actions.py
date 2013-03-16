#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir="."

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    fixperms("%s-%s/wallpapers" % (get.srcNAME(), get.srcVERSION()))

def install():
    pisitools.insinto("%s/share/" % get.defaultprefixDIR(), "%s-%s/wallpapers" % (get.srcNAME(), get.srcVERSION()))

    pisitools.insinto("%s/share/" % get.defaultprefixDIR(), "sample-files", "example-content")

