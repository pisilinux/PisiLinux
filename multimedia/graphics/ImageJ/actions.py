#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant -f source/build.xml build")

def install():
    pisitools.insinto("/usr/share/java", "source/ij.jar", "ij.jar")

    pisitools.dodir("/usr/share/ImageJ/plugins")

    pisitools.dodoc("source/release-notes.html")

