#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")
    shelltools.export("JAVA_HOME","/opt/sun-jdk")
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant jar")
    shelltools.system("touch LICENSE.txt")
    
def install():
    pisitools.insinto("/usr/share/java","dist/commons-codec-1.6-SNAPSHOT.jar","commons-codec.jar")
    
    pisitools.dodoc("LICENSE*", "RELEASE*", "TODO")