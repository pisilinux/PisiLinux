#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/opt/icecream \
                         --localstatedir=/var \
                         --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    """
    for chost in ["", "%s-pc-linux-gnu-" % get.ARCH()]:
        for i in ["c++", "cc", "g++", "gcc"]:
            pisitools.dosym("icecc", "/opt/icecream/bin/%s%s" % (chost, i))
    """
