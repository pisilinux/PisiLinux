#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "pynifti-%s" % get.srcVERSION().split("_")[1]

def setup():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("AUTHOR", "COPYING", "Changelog", "PKG-INFO", "TODO")
    pisitools.doman("man/*")
