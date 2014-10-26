#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dodir("m2_repo")
    
    shelltools.system("mvn package -Dmaven.repo.local='m2_repo' -Dmaven.test.skip=true")

def check():
    shelltools.system("mvn -Dmaven.repo.local='m2_repo' test")

def install():
    pisitools.dodir("/etc/ssl/certs/java")
    pisitools.insinto("/etc/default/", "debian/default", "cacerts")
    pisitools.insinto("/usr/share/ca-certificates-java/", "target/ca-certificates-java-20140324.jar", "ca-certificates-java.jar")