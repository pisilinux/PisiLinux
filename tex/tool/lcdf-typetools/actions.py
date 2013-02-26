#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-kpathsea=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.install()

    # Otfinfo also comes with openmpi. These two packages are not identical
    # but they have the same name. We rename this one to avoid conflicts
    pisitools.domove("/usr/bin/otfinfo", "/usr/bin", "otfinfo-lcdf")

    pisitools.dodoc("ONEWS", "NEWS", "README")
