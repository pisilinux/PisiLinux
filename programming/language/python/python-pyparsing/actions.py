#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def install():
    pythonmodules.install()
    liste = ["examples/*", "docs/pycon06-AdventureEngineUsingPyparsing-notes.pdf", "docs/pycon06-IntroToPyparsing-notes.pdf"]
    for i in liste:
        pisitools.insinto("%s/%s/examples" % (get.docDIR(), get.srcNAME()),"%s" % i)

    pisitools.dohtml("HowToUsePyparsing.html","htmldoc/*")
    pisitools.dodoc("LICENSE", "CHANGES", "README")
