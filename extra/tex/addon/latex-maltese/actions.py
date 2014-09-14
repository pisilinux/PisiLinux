#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "maltese"

def build():
    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("tex", "dtx")):
            shelltools.system("texi2dvi -v -c --language=latex %s" % srcfile)
    shelltools.system("texi2dvi -v -c --language=latex ./maltese.dtx")

def install():
    for srcfile in shelltools.ls("."):
        if srcfile.endswith(("dvi", "ps", "pdf")):
            pisitools.dodoc(srcfile)
            pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), srcfile), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, srcfile))
        elif srcfile.endswith(("sty", "cls", "fd", "clo", "def", "cfg")):
            pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, srcfile)

    pisitools.dodoc("README.txt")
