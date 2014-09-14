#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

WorkDir = "Jinja2-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.insinto(examples, "examples/*")

    #Create docs with python-Sphinx
    shelltools.cd("docs")
    autotools.make("html")
    shelltools.cd("..")

    pisitools.dohtml("docs/_build/html/*")
    pisitools.dodoc("CHANGES")
