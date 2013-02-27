#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

WorkDir = "%s-%s" % (get.srcNAME()[7:], get.srcVERSION().replace("_","-"))

def build():
    pythonmodules.compile()

def setup():
    shelltools.chmod("examples/*", 0644)
    shelltools.cd("documentation")
    autotools.make("html")
    shelltools.cd("..")

def install():
    pythonmodules.install()
    pisitools.insinto(examples, "examples/*")
    pisitools.dohtml("documentation/_build/html/*")

    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "README.txt")
