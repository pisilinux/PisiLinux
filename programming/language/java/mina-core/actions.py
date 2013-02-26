#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mina-%s" % get.srcVERSION()

shelltools.export("JAVA_HOME","/opt/sun-jdk")

def setup():
    shelltools.unlinkDir("%s/mina-%s/core/src/test" % (get.workDIR(), get.srcVERSION()))

def build():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "dist/mina-core.jar")

    pisitools.dodoc("LICENSE*", "NOTICE.txt")
    shelltools.copytree("dist/docs", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))

