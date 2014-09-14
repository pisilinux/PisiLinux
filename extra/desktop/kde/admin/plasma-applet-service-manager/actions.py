#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def install():
    applet_name = "systemservices"
    package_dir = "%s-%s" % (applet_name, get.srcVERSION())
    pisitools.insinto("/usr/share/kde4/apps/plasma/plasmoids/", package_dir, applet_name)
    pisitools.insinto("/usr/share/kde4/services/", "%s/metadata.desktop" % package_dir, "plasma-applet-%s.desktop" % applet_name)

