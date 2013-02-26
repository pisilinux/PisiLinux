#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "DropboxServiceMenu-%s" % get.srcVERSION()

def install():
    pisitools.dobin("dropbox-scripts/*")

    pisitools.insinto("/usr/share/kde4/services/ServiceMenus", "*.desktop")

    pisitools.dodoc("Changelog", "LICENSE", "THANKS")
