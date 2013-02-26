#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    """
    for d in ["et", "sv", "uk"]:
        pisitools.remove("/usr/kde/4/share/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
        pisitools.dosym("/usr/kde/4/share/doc/HTML/en/common", "/usr/kde/4/share/doc/HTML/%s/%s/common" % (d, get.srcNAME()))
    """

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
