#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="svninfo"

def build():
    shelltools.export("VARTEXFONTS", get.curDIR())

    shelltools.system("/usr/bin/latex --interaction=batchmode ./svninfo.ins")
    shelltools.system("/usr/bin/texi2dvi -q -c --language=latex ./svninfo.dtx")
    autotools.make("-j1")

def install():
    for dvidoc in ["dvi", "pdf", "ps"]:
        print dvidoc
        pisitools.dodoc("svninfo.%s" % dvidoc)
        pisitools.dosym("/usr/share/doc/%s/svninfo.%s" % (get.srcTAG(), dvidoc), "/usr/share/texmf/doc/latex/svninfo/svninfo.%s" %  dvidoc)

    for stylesdoc in ["sty", "cfg"]:
        print stylesdoc
        pisitools.insinto("/usr/share/texmf/tex/latex/svninfo/", "*.%s" %stylesdoc)

    pisitools.dodoc("README")
