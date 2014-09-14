#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
Jdir = "/usr/share/java"
shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

def setup():
    shelltools.system("unzip -oq src.zip -d src")
    shelltools.cd("src")
    shelltools.system("./build.sh")

def build():
    shelltools.cd("src")
    shelltools.system("ant -f ../build-swt.xml compile")

def install():
    shelltools.cd("src")
    pisitools.insinto("/usr/lib/", "*gtk-4335.so")
    pisitools.insinto("/usr/share/java/", "../swt.jar", "swt-4.3.2.jar")
    pisitools.dosym("%s/swt-4.3.2.jar" % Jdir, "%s/swt.jar" % Jdir)
    pisitools.dosym("%s/swt-4.3.2.jar" % Jdir, "%s/zekr/lib/swt.jar" % Jdir)
    shelltools.system("ant -f ../build-swt.xml jar")

    pisitools.dodoc("./about_files/*.txt")
