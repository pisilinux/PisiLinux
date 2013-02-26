#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "pyosd-%s" % get.srcVERSION()
mods = "%s/%s/modules" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.chmod("modules/*", 0644)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "COPYING", "README*")
    pisitools.dohtml("pyosd.html")
    pisitools.insinto(mods, "modules/*")

