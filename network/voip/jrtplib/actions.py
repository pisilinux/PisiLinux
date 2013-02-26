#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    #autotools.configure("--disable-static")
    cmaketools.configure()

def build():
    cmaketools.make("-j1")

def install():
    cmaketools.install()

    pisitools.dodoc("ChangeLog", "README.TXT", "LICENSE.MIT", "TODO")
