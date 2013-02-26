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
from pisi.actionsapi import pythonmodules

def build():
    pythonmodules.compile()
    autotools.make("-C doc html")
    autotools.make("-C doc man")

def install():
    pythonmodules.install()
    pisitools.dohtml("doc/_build/html/")
    pisitools.doman("doc/_build/man/py.1")
    pisitools.insinto("%s/python-py" % get.docDIR(), "doc/example")

