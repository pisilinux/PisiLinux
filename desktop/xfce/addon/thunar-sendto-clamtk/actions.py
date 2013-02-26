#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/Thunar/sendto/", "thunar-sendto-clamtk.desktop")
    pisitools.dodoc("CHANGES", "DISCLAIMER", "LICENSE", "README")
    pisitools.doman("thunar-sendto-clamtk.1.gz")
