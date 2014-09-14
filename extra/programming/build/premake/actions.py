#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("verbose=1 -C build/gmake.unix/")

def install():
    pisitools.dobin("bin/release/premake4")
    pisitools.dosym("/usr/bin/premake4", "/usr/bin/premake")
    pisitools.doman("premake4.1")

    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "README.txt")
