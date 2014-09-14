#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

dataDir = "%s/%s/" % (get.dataDIR(), get.srcNAME())

def setup():
    MocFilesToRemove=shelltools.ls("moc_*")
    for i in MocFilesToRemove:
        shelltools.unlink(i)

    shelltools.system("qmake QMAKE_CXXFLAGS_RELEASE=\'%s\'" % get.CXXFLAGS())

def build():
    autotools.make("-j1")

def install():
    pisitools.dodir(dataDir)
    pisitools.dobin("clustalx")

    for i in ["colprot.xml", "coldna.xml", "colprint.xml", "clustalx.hlp"]:
        pisitools.insinto(dataDir, i);

    pisitools.dodoc("README", "COPYING*")

