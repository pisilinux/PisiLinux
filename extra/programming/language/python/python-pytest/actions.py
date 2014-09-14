#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules


def build():
    pythonmodules.compile()
    autotools.make("-C doc en")
    autotools.make("-C doc ja")


def install():
    pythonmodules.install()
    #pisitools.dohtml("doc/en/html/")
    #pisitools.doman("doc/_build/man/pytest.1")
    pisitools.insinto("%s/python-pytest" % get.docDIR(), "doc/en/example")
