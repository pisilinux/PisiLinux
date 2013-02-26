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

def setup():
    shelltools.makedirs("src/main/java")
    shelltools.makedirs("src/test/java")
    shelltools.system("unzip junit-%s-src.jar -d src/main/java" % get.srcVERSION())

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant build jars")

def install():
    pisitools.insinto("/usr/share/java", "junit-%s.jar" % get.srcVERSION(), "junit.jar")
    pisitools.insinto("/usr/share/java", "junit-dep-%s.jar" % get.srcVERSION(), "junit-dep.jar")

    pisitools.dohtml("cpl-v10.html", "README.html")
    pisitools.dodoc("doc/*.txt")
