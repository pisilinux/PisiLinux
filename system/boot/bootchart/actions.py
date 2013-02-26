#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("CFLAGS='%s'" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s \
                          PY_LIBDIR=/usr/lib/%s \
                          NO_PYTHON_COMPILE=1" % (get.installDIR(), get.curPYTHON()))

    pisitools.dosym("pybootchartgui", "/usr/bin/bootchart")

    pisitools.dodoc("COPYING", "README*")

