#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Xonotic"

def install():
    pisitools.insinto("/usr/share/xonotic/data", "data/*")

    pisitools.dodoc("COPYING", "GPL-2", "GPL-3")
    # pisitools.dodoc("Docs/*")
