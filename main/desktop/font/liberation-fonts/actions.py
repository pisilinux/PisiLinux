#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "liberation-fonts-ttf-2.00.0"


def install():
    pisitools.insinto("/usr/share/fonts/liberation-fonts/", "*.ttf")

    pisitools.dodoc("LICENSE", "AUTHORS", "ChangeLog", "README")
