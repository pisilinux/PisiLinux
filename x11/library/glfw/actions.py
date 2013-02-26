#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("compile.sh", '(GLFW_LFLAGS="\$LFLAGS\s-lGL)"', r'\1 -lrt"')
    autotools.make("x11")

def install():
    autotools.make("DESTDIR=%s x11-install" % get.installDIR())

    pisitools.dohtml("readme.html")
    pisitools.dodoc("docs/*")
