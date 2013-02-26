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
from pisi.actionsapi import shelltools

WorkDir="svninfo-%s" % get.srcVERSION()

def build():
    shelltools.export("VARTEXFONTS", get.curDIR())

    shelltools.system("latex --interaction=batchmode ./svninfo.ins")
    shelltools.system("texi2dvi -q -c --language=latex ./svninfo.dtx")
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
