#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/usr/share/warmux/map", "*")

    # These are now in the main Warmux distribution
    pisitools.removeDir("/usr/share/warmux/map/urbanheights")

    pisitools.remove("/usr/share/warmux/map/README")
    pisitools.remove("/usr/share/warmux/map/pisiBuildState")
