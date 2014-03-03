#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("JAVAC","/usr/lib/jvm/java-7-openjdk/bin/javac")
    shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant")

def install():
    pisitools.dobin("bin/umlgraph")

    pisitools.insinto("/usr/share/java", "lib/*")

    pisitools.dohtml("doc/")
    pisitools.dohtml("javadoc/")
