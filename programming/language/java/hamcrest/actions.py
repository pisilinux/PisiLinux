#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.export("JAVA_HOME", "/opt/sun-jdk")
    shelltools.system("ant core")

def install():
    pisitools.insinto("/usr/share/java", "build/hamcrest-core-SNAPSHOT.jar", "hamcrest.jar")

    pisitools.dodoc("CHANGES.txt", "LICENSE.txt", "README.txt")
