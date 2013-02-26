#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip="/"

shelltools.export("JAVA_HOME", "/opt/sun-jdk")

jabrefDir = "/usr/share/java/"

def setup():
    shelltools.export("LC_ALL", "C")
    shelltools.system("ant")

def install():
    shelltools.cd("build")

    pisitools.dodir(jabrefDir)

    pisitools.insinto( "%s" % jabrefDir, "lib/JabRef-2.7.jar")

