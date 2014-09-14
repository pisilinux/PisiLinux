#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DLIBRARY_INSTALL_DIR=/usr/lib")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("ChangeLog", "README.TXT", "LICENSE.MIT", "TODO")