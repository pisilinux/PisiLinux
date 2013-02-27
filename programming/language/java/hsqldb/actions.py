#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "hsqldb"

def setup():
    shelltools.unlink("lib/hsqldb.jar")

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.cd("build")
    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/share/java", "lib/hsqldb.jar")

    pisitools.dohtml("doc/*.html", "doc/guide/*", "docsrc/*")
    pisitools.dodoc("readme.txt", "doc/*.txt")
