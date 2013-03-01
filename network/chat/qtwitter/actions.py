#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import qt4
from pisi.actionsapi import pisitools

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()
    pisitools.dodoc("CHANGELOG", "LICENSE", "README")
