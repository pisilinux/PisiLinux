#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("JAVAC","/opt/sun-jdk/bin/javac")
shelltools.export("JAVA_HOME","/opt/sun-jdk")

def build():
    pisitools.dosed("Makefile", "Class\-Path\: \$\(JARDIR\)\/hexdump.jar", "Class-Path: hexdump.jar")
    autotools.make("-j1")

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("changelog", "COPYING", "README")

