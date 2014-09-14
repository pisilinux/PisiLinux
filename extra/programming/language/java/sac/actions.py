#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("src")
    shelltools.export("JAVAC","/usr/lib/jvm/java-7-openjdk/bin/javac")
    shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant jar")
    shelltools.system("touch LICENSE.txt")
    
def install():
    pisitools.insinto("/usr/share/java","dist/sac.jar")
    
    pisitools.dodoc("LICENSE.txt", "COPYRIGHT.html")