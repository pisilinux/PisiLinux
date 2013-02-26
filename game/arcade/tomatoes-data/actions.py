#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tomatoes-%s" % get.srcVERSION()
ketchup = "/usr/share/tomatoes"

def install():
    pisitools.dodir("%s/music" % ketchup)
    pisitools.insinto(ketchup, "tomatoes.mpk")
    pisitools.insinto("%s/music" % ketchup, "music/IHaveNoTomatoes.it")

