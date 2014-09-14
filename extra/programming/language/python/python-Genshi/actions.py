#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())
htmltxt = "%s/%s/html" % (get.docDIR(), get.srcNAME())

WorkDir = "Genshi-%s" % get.srcVERSION()

def setup():
    shelltools.chmod("examples/*", 0644)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dohtml("doc/")
    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(htmltxt, "doc/*.txt")

