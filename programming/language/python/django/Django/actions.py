#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

    shelltools.cd("docs")
    autotools.make("html")

def install():
    pythonmodules.install()

    shelltools.copytree("docs/_build/html", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))
