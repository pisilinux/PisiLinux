#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "%s" % get.srcNAME()

def build():
#changed for version 4.2.4
    autotools.make('-f makefile.unix')
#autotools.make for older version
#    autotools.make('-f makefile.unix \
#                    CXXFLAGS="%s" \
#                    CXX="%s" \
#                    STRIP="true"' % (get.CXXFLAGS(), get.CXX()))

def install():
    pisitools.dobin("unrar")

    pisitools.dodoc("readme.txt","license.txt")
