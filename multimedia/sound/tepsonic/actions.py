#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.install("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE", "README*")
