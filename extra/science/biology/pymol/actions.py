#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = get.srcNAME()

def setup():
    pisitools.dosed("pymol", "@PYTHONDIR@", "/usr/lib/%s" % get.curPYTHON())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    #Now do the dirty work of setup2.py script
    for d in ("data", "test", "scripts", "examples"):
        shelltools.copytree(d, "%s/usr/lib/%s/site-packages/pymol/" % (get.installDIR(), get.curPYTHON()))

    pisitools.dobin("pymol")
