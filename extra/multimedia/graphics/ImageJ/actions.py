#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def build():
    shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
    shelltools.system("ant -f source/build.xml build")

def install():
    pisitools.insinto("/usr/share/java", "source/ij.jar", "ij.jar")

    pisitools.dodir("/usr/share/ImageJ/plugins")

    pisitools.dodoc("source/release-notes.html")

