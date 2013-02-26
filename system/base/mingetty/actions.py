#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mingetty-1.08"

def build():
    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    pisitools.dosbin("mingetty", "/sbin")
    pisitools.doman("mingetty.8")
    #pisitools.insinto("/usr/share/locale/tr/LC_MESSAGES", "tr.mo")

    pisitools.dodoc("COPYING")