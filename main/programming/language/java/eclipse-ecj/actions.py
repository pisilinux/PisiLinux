#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
shelltools.export("LC_ALL", "C")

def setup():
    shelltools.export("LANG", "en_US.UTF-8")
    shelltools.system("sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml")
    shelltools.system('sed -i -e "s/Xlint:none/Xlint:none -encoding cp1252/g" build.xml')
    shelltools.system("ant build")

def install():    
    pisitools.insinto("/usr/share/man/man1/","ecj.1")
    
    pisitools.insinto("/usr/share/java/", "ecj.jar", "eclipse-ecj-4.4.jar")
    
    shelltools.cd("%s/usr/share/java/" % get.installDIR())
    
    pisitools.dosym("eclipse-ecj-4.4.jar", "/usr/share/java/ecj.jar")
    pisitools.dosym("eclipse-ecj-4.4.jar", "/usr/share/java/eclipse-ecj.jar")