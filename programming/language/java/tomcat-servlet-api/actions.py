#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="apache-tomcat-%s-src/servletapi" % get.srcVERSION()

shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")
shelltools.export("JAVA_HOME","/opt/sun-jdk")

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant -f jsr154/build.xml dist")
    shelltools.system("ant -f jsr152/build.xml dist")

def install():
    pisitools.insinto("/usr/share/java","jsr154/dist/lib/servlet-api*.jar","servlet-api.jar")
    pisitools.insinto("/usr/share/java","jsr152/dist/lib/jsp-api*.jar","jsp-api.jar")

    pisitools.dodoc("jsr154/dist/README.txt")
    pisitools.dodoc("jsr154/dist/LICENSE")
