#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/Thunar/sendto/", "thunar-sendto-clamtk.desktop")
    pisitools.dodoc("CHANGES", "DISCLAIMER", "LICENSE", "README")
    pisitools.doman("thunar-sendto-clamtk.1.gz")
