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

WorkDir = "pyv4l-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    shelltools.chmod("examples/*", 0644)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("COPYING")
    pisitools.dohtml("doc/*")

    pisitools.insinto(examples, "examples/*")

