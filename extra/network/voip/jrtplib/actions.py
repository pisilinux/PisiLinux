#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr")
    pisitools.dosed("CMakeCache.txt", "LIBRARY_INSTALL_DIR:PATH=lib64", "LIBRARY_INSTALL_DIR:PATH=lib")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("ChangeLog", "README.TXT", "LICENSE.MIT", "TODO")