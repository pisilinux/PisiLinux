#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
			  -DCMAKE_BUILD_TYPE=release ")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("CHANGELOG", "CREDITS", "README", "README.*", "doc/version-spec.txt")
