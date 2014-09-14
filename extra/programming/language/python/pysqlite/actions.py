#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

code = "%s/%s/code" % (get.docDIR(), get.srcNAME())

def build():
    pisitools.dosed("setup.py", "pysqlite2-doc", "share/doc/pysqlite")
    pythonmodules.compile("build_docs")

def setup():
    shelltools.chmod("doc/includes/sqlite3/*", 0644)

def install():
    pythonmodules.install()

    pisitools.dohtml("build/doc/")
    pisitools.insinto(code, "doc/includes/sqlite3/*")
    pisitools.remove("%s/%s/install-source.txt" % (get.docDIR(), get.srcNAME()))

