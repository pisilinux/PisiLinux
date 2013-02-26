#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.unlink("po/*.po")

    pythonmodules.run("setup.py configure --no-install-init \
                                          --no-install-kde \
                                          --resume=/usr/share/wicd/scripts \
                                          --suspend=/usr/share/wicd/scripts \
                                          --verbose")

def build():
    pythonmodules.compile("build")
    pythonmodules.compile("compile_translations")

def install():
    pythonmodules.install()
