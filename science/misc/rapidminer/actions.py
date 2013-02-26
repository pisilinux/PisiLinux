#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = get.srcNAME()

shelltools.export("JAVA_HOME", "/opt/sun-jdk")

def setup():
    shelltools.system("ant clean")

def build():
    shelltools.system("ant createJar")

def install():
    pisitools.insinto("/usr/share/java/rapidminer", "lib/*")

