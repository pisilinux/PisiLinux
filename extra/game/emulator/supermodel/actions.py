#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("-f Makefiles/Makefile.SDL.UNIX.GCC -j1")

def install():
    pisitools.dobin("bin/Supermodel", "/opt/supermodel")

    pisitools.insinto("/opt/supermodel/Config", "Config/*")

    shelltools.chmod("%s/opt/supermodel/Config/Supermodel.ini" % get.installDIR(), 0644)

    pisitools.dodoc("Docs/*")
