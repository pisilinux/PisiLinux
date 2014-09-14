#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
    shelltools.system("javac -target 1.6 -source 1.6 -cp \".\" UpdateCertificates.java")
    shelltools.system("jar cfe ca-certificates-java.jar UpdateCertificates *.class")

def check():
    pass
    # needs junit compiled againist openjdk
    #shelltools.system("javac -cp /usr/share/java/junit.jar:/usr/share/ca-certificates-java/ca-certificates-java.jar \
                    #UpdateCertificatesTest.java Exceptions.java")
    #shelltools.system("java -cp /usr/share/java/junit.jar:/usr/share/ca-certificates-java/ca-certificates-java.jar:. \
                    #org.junit.runner.JUnitCore \
                    #UpdateCertificatesTest")

def install():
    pisitools.dodir("/etc/ssl/certs/java")
    pisitools.insinto("/etc/default/", "debian/default", "cacerts")
    pisitools.insinto("/usr/share/ca-certificates-java/", "ca-certificates-java.jar")

