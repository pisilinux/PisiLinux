#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "currvita"

shelltools.export("HOME", get.workDIR())

def build():
    shelltools.system("latex --interaction=batchmode currvita.ins")

    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("tex", "dtx")):
            shelltools.system("texi2dvi -q -c --language=latex %s" % srcfile)

def install():
    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("dvi", "ps", "pdf")):
            pisitools.dodoc(srcfile)
            pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), srcfile), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, srcfile))
        elif srcfile.endswith(("sty", "cls", "fd", "clo", "def", "cfg")):
            pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, srcfile)

    pisitools.dodoc("README")
