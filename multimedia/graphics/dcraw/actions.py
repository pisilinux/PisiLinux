#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "dcraw"

def build():
    autotools.compile('-DLOCALEDIR="\\"/usr/share/locale\\"" -lm -ljasper -llcms -ljpeg -o dcraw dcraw.c')

def install():
    pisitools.dobin("dcraw")
    pisitools.doman("dcraw.1")

    # Build catalogs
    for f in shelltools.ls("*.po"):
        pisitools.domo(f, f.split("dcraw_")[1].split(".po")[0], "dcraw.mo")