#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="dvipdfm"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/usr/share/texmf/fonts/map/dvipdfm/base")
    for i in ["cmr", "psbase14", "lw35urw", "lw35urwa", "t1fonts"]:
        pisitools.domove("/usr/share/texmf/dvipdfm/config/%s.map" % i, "usr/share/texmf/fonts/map/dvipdfm/base")

    pisitools.dodir("/usr/share/texmf/fonts/enc/dvipdfm/")
    shelltools.move("%s/usr/share/texmf/dvipdfm/base" % get.installDIR(), "%s/usr/share/texmf/fonts/enc/dvipdfm/base" % get.installDIR())

    pisitools.insinto("/usr/share/texmf/tex/latex/dvipdfm/", "latex-support/dvipdfm.def")

    pisitools.dodoc("AUTHORS", "ChangeLog", "Credits", "NEWS", "OBTAINING", "README*", "TODO", "doc/*", "latex-support/*")
