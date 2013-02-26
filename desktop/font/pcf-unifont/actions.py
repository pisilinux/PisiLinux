#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.insinto("/usr/share/fonts/unifont/","*.pcf")

