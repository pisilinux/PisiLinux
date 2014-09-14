#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "hsqldb-2.3.1"

def build():
    shelltools.cd("hsqldb")
    shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
    shelltools.cd("build")
    shelltools.system("ant hsqldb")

def install():
    shelltools.cd("hsqldb")
    pisitools.insinto("/usr/share/java", "lib/hsqldb.jar")      
    pisitools.dohtml("doc/*.html", "doc/guide/*", "doc-src/*")
    pisitools.dodoc("readme.txt", "doc/*.txt")
