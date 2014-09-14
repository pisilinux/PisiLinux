#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Grounation-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/icons", "Grounation*")
    pisitools.removeDir("/usr/share/icons/*/Source")

    pisitools.dodoc("COPYING", "NEWS", "README")
