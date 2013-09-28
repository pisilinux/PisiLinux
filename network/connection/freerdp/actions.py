#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get


def setup():
    cmaketools.configure()

def build():
    cmaketools.make("-j1")

#def check():
#    autotools.make("-j1 test")

def install():
    cmaketools.install("libdir=%s/usr/lib" % get.installDIR())

    pisitools.dodoc("LICENSE", "README", )
