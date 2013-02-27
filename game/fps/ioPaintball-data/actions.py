#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = "/"
datadir = "/usr/share/ioPaintball/paintball"

def install():
    for data in ["paintball/pak0.pk3", "paintball/*.cfg"]:
        pisitools.insinto(datadir, data)

    pisitools.dodoc("*.txt", "paintball/description.txt")
