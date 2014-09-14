#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("gtk")
    autotools.configure("--prefix=/usr  \
                         --with-sdd1-decomp \
                         --with-netplay \
                         --with-opengl")

def build():
    shelltools.cd("gtk")
    autotools.make()

def install():
    shelltools.cd("gtk")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    shelltools.cd("docs")
    pisitools.dodoc("snes9x.conf.default", "*.txt")
