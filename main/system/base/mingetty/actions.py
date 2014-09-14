#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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