#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    shelltools.cd("lib/irrlicht/source/Irrlicht")
    autotools.make("NDEBUG=1")
    shelltools.cd("../../../../")
    cmaketools.configure()

def build():
    cmaketools.make("V=1 -j2")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "COPYING", "TODO")

