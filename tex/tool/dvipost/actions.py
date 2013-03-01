#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("dvipost")

    for i in ["/usr/bin/pptex", "/usr/bin/pplatex"]:
        pisitools.dosym("/usr/bin/dvipost", i)

    pisitools.insinto("/usr/share/texmf/tex/latex/misc/", "dvipost.sty")
    shelltools.chmod(get.installDIR() + "/usr/share/texmf/tex/latex/misc/dvipost.sty", 0644)

    shelltools.move("dvipost.man", "dvipost.1")
    pisitools.doman("dvipost.1")

    pisitools.dohtml("dvipost.html")

    pisitools.dodoc("dvipost.doc", "CHANGELOG", "NOTES", "README")
