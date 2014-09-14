#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "mscore-%s/mscore" % get.srcVERSION()

def setup():
    pisitools.dosed("mscore/genft.cpp", "freetype/tttables.h", "freetype2/tttables.h")
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_SKIP_RPATH=TRUE", sourceDir="..")
    #shelltools.export("CFLAGS", "%s -I/usr/include/freetype2" % get.CFLAGS())

def build():
    shelltools.cd("build")

    cmaketools.make("lupdate")
    cmaketools.make("lrelease")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())


    shelltools.cd("..")
    pisitools.dodoc("ChangeLog", "NEWS", "README*", "ChangeLog")
    pisitools.doman("packaging/*.1")
