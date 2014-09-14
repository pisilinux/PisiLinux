#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.export("CXXFLAGS", "%s -Wno-deprecated -fno-strict-aliasing -fpermissive" % get.CXXFLAGS())
    autotools.configure()

def build():
    shelltools.export("LC_ALL", "C")
    shelltools.cd("ddd")
    autotools.make("version.h build.h host.h root.h configinfo.C Ddd.ad.h")

    shelltools.cd("..")
    autotools.make()

def install():
    shelltools.export("LC_ALL", "C")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # using wrapper script for now
    pisitools.rename("/usr/bin/ddd", "ddd.bin")

    pisitools.dodoc("AUTHORS", "COPYING*", "CREDITS", "NEWS*", "PROBLEMS", "README*", "TIPS", "TODO")

