#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
