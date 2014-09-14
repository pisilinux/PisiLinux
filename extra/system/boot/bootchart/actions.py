#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "^(DOCDIR\s\?=\s\/usr\/share\/doc)s(.*)", r"\1\2")
    autotools.make("CFLAGS='%s'" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s \
                          PY_LIBDIR=/usr/lib/%s \
                          NO_PYTHON_COMPILE=1" % (get.installDIR(), get.curPYTHON()))

    pisitools.dosym("pybootchartgui", "/usr/bin/bootchart")

    pisitools.dodoc("COPYING", "README*")

