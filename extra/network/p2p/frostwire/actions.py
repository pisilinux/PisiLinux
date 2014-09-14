#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s.noarch" % (get.srcNAME(), get.srcVERSION())

def install():
    pisitools.insinto("/usr/share/frostwire", "*")
    pisitools.insinto("/usr/share/applications", "frostwire.desktop")
    pisitools.dosym("/usr/share/frostwire/frostwire", "/usr/bin/frostwire")

    pisitools.dodoc("changelog", "COPYING", "EULA*")
