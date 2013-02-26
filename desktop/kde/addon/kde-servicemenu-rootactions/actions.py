#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "rootactions_servicemenu_%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/kde4/services/ServiceMenus", "Root_Actions_%s/dolphin-KDE4/*.desktop" % get.srcVERSION())
    pisitools.dobin("Root_Actions_%s/rootactions-servicemenu.pl" % get.srcVERSION())

    pisitools.dodoc("README")
