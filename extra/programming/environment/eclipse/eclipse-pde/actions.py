#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.dodir("/opt")
    pisitools.insinto("/opt/eclipse", "plugins")
    pisitools.insinto("/opt/eclipse", "features")
