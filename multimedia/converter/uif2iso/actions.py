#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.dobin("src/uif2iso")

    pisitools.dodoc("uif2iso.txt", "README")
