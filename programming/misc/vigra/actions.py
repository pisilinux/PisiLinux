#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION())
NoStrip=["/usr/share/doc"]

def setup():
    cmaketools.configure("-DWITH_VIGRANUMPY=1 -DDOXYGEN_FOUND=0")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("README*", "LICENSE*")
