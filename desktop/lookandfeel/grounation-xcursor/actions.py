#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Grounation-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/icons", "Grounation*")
    pisitools.removeDir("/usr/share/icons/*/Source")

    pisitools.dodoc("COPYING", "NEWS", "README")
