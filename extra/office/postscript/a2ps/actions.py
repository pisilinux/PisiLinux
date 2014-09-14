#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/liba2ps.a")

    # texi2dvi4a2ps script removed for unneeded texlive-bin dependency
    pisitools.remove("/usr/bin/texi2dvi4a2ps")

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "ChangeLog", "FAQ", "NEWS", "README*", "THANKS", "TODO")
