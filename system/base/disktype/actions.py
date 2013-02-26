#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CCACHE_DIR", "%s" % get.workDIR())
    autotools.make('CFLAGS="%s -fno-stack-protector -fno-strict-aliasing"' % get.CFLAGS())

def install():
    pisitools.dobin("disktype")
    pisitools.doman("disktype.1")
    pisitools.dodoc("README", "HISTORY", "TODO")
