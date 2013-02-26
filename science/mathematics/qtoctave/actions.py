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

WorkDir = "qtoctave-0.9.1"

def setup():
    cmaketools.configure("-DCMAKE_SKIP_RPATH:STRING=ON")

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.install()

    pisitools.removeDir("%s/octave-html" % get.docDIR())

    pisitools.dodoc("LICENSE_GPL.txt", "readme.txt")
