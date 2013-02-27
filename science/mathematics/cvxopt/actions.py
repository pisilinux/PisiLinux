#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.cd("src")
    pythonmodules.install()

    shelltools.cd("..")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcNAME() , "examples")
