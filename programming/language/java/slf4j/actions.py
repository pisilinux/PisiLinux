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

shelltools.export("JAVA_HOME","/opt/sun-jdk")
shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")

def setup():
    shelltools.system("ant clean")

def build():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/java", "dist/*.jar")

    pisitools.dodir(get.docDIR())
    shelltools.copytree("dist/docs", "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))
    pisitools.dodoc("LICENSE.txt")

