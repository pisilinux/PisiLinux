#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gle-graphics-%sc" % get.srcVERSION()

def setup():
    autotools.configure("--with-x \
                         --with-rpath=no \
                         --with-qt=/usr/lib/qt4")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/lib/pkgconfig")

    pisitools.dodoc("README.txt", "LICENSE.txt")
