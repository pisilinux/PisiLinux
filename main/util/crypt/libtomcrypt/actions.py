#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def build():
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

