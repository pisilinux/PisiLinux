#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


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
