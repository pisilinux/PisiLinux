#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "lshw-B.%s" % get.srcVERSION()

def setup():
    pisitools.dosed("src/Makefile", "^CXX\?.*", "CXX=%s" % get.CXX())
    pisitools.dosed("src/core/Makefile", "^CXX=.*", "CXX=%s" % get.CXX())
    pisitools.dosed("src/Makefile", "\$\(RPM_OPT_FLAGS\)", "%s" % get.CXXFLAGS())
    pisitools.dosed("src/core/Makefile", "\$\(RPM_OPT_FLAGS\)", "%s" % get.CXXFLAGS())

def build():
    autotools.make()
    autotools.make("gui")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-gui")

    pisitools.dodoc("docs/*", "COPYING", "README")
