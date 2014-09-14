#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "blobby-beta-%s" % get.srcVERSION()

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    for bin in ["src/blobby", "src/blobby-server"]:
        pisitools.dobin(bin)

    for data in ["data/backgrounds", "data/gf2x", "data/gfx", "data/sounds", "data/scripts", "data/*.xml"]:
        pisitools.insinto("/usr/share/blobby", data)

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO", "doc/*.txt")
