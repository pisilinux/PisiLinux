#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    applet_name = "systemservices"
    package_dir = "%s-%s" % (applet_name, get.srcVERSION())
    pisitools.insinto("/usr/share/kde4/apps/plasma/plasmoids/", package_dir, applet_name)
    pisitools.insinto("/usr/share/kde4/services/", "%s/metadata.desktop" % package_dir, "plasma-applet-%s.desktop" % applet_name)

