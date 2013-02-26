#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -I/usr/include/squirrel" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -I/usr/include/squirrel" % get.CXXFLAGS())
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DINSTALL_SUBDIR_SHARE=share/supertux2 -DINSTALL_SUBDIR_BIN=bin", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.remove("%s/%s2/INSTALL" % (get.docDIR(), get.srcNAME()))
    pisitools.dodoc("docs/*")
