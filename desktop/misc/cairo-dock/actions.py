#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    pisitools.dodoc("ChangeLog", "INSTALL", "LICENSE", "LGPL-2", "copyright")
