#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pisitools.insinto("/usr/share/fonts/ubuntu/", "*.ttf")
    shelltools.chmod("%s/usr/share/fonts/ubuntu/*" % get.installDIR(), 0644)

    pisitools.dodoc("*.txt")
