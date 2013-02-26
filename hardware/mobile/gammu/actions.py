#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DENABLE_SHARED=ON\
    -DINSTALL_DOC=ON\
    -DINSTALL_LOC=ON\
    -DINSTALL_BASH_COMPLETION=OFF", installPrefix="%s/usr" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall()

    pisitools.dodoc("ChangeLog", "COPYING", "README")

    #pisitools.remove("/usr/lib/*.a")
