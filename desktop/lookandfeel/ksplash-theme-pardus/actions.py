#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

WorkDir = "./"

def install():
    pisitools.insinto("%s/ksplash/Themes/" % kde4.appsdir, "ksplash-pardus-theme", "Pardus")
    pisitools.insinto("%s/ksplash/Themes/" % kde4.appsdir, "ksplash-pardus-theme-milky", "Pardus-Milky")

