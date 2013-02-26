#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = "MemonixSourceCode"

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    pisitools.dobin("Memonix")

    pisitools.dodoc("gpl-3.0.txt", "License.txt", "ReadMe.txt")
