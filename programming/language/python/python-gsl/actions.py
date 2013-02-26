#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("examples/*", destDir="%s/examples" % get.srcNAME())

    pisitools.dodoc("ChangeLog", "COPYING", "CREDITS", "PKG-INFO", "README", "TODO")
