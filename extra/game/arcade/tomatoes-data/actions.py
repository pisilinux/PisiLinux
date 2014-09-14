#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tomatoes-%s" % get.srcVERSION()
ketchup = "/usr/share/tomatoes"

def install():
    pisitools.dodir("%s/music" % ketchup)
    pisitools.insinto(ketchup, "tomatoes.mpk")
    pisitools.insinto("%s/music" % ketchup, "music/IHaveNoTomatoes.it")

