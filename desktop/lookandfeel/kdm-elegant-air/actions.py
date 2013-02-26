#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

WorkDir = "./"

def install():
    pisitools.insinto("%s/kdm/themes/" % kde4.appsdir, "Anka-Elegant-Air_KDM", "Anka-Elegant-Air")