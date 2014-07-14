#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir= "g-brief"

def build():
    #These files will be created by latex command below
    for i in ["beispiel2.tex", "beispiel.tex"]:
        shelltools.unlink(i)

    shelltools.system("/usr/bin/latex --interaction=batchmode g-brief.ins")

    for srcfile in shelltools.ls("."):
        if srcfile.endswith("tex"):
            shelltools.system("/usr/bin/texi2dvi -q -c --language=latex %s" % srcfile)

def install():
    dvidocs = []
    for i in ["dvi", "pdf"]:
        dvidocs.extend(shelltools.ls("*.%s" % i))
    for dvidoc in dvidocs:
        print dvidoc
        pisitools.dodoc(dvidoc)
        pisitools.dosym("/usr/share/doc/%s/%s" % (get.srcTAG(), dvidoc), "/usr/share/texmf/doc/latex/%s/%s" % (WorkDir, dvidoc))

    for stylesdoc in ["sty", "cls"]:
        print stylesdoc
        pisitools.insinto("/usr/share/texmf/tex/latex/%s/" % WorkDir, "*.%s" % stylesdoc)

