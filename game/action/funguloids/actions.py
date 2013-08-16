#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "funguloids"

def setup():
    #shelltools.export("CXXFLAGS", "%s -Wno-deprecated" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "-lboost_system")
    shelltools.system("sh sed.sh")
    libtools.libtoolize()
    autotools.autoreconf("-fi")
    autotools.configure("--without-fmod \
                         --with-openal \
                         --with-ogg \
                         --with-mad")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/share/docs", "doc")
    pisitools.dodoc("COPYING", "README")
