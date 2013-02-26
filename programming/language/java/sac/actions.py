#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("src")
    shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")
    shelltools.export("JAVA_HOME","/opt/sun-jdk")
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant jar")
    shelltools.system("touch LICENSE.txt")
    
def install():
    pisitools.insinto("/usr/share/java","dist/sac.jar")
    
    pisitools.dodoc("LICENSE.txt", "COPYRIGHT.html")