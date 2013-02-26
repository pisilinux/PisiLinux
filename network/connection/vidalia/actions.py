#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure(installPrefix = "/%s" % (get.defaultprefixDIR()))

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("CHANGELOG", "CREDITS", "README", "README.*", "doc/version-spec.txt")
