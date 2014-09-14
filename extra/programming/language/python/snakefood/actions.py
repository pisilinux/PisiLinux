#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.doman("doc/manpages/*.1")
    pisitools.dohtml("index.html")
    pisitools.dohtml("doc/*")
    pisitools.insinto("/usr/share/doc/snakefood/examples", "doc/examples/*")

    pisitools.dodoc("CHANGES", "TODO", "VERSION")

