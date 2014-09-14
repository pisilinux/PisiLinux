#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

def build():
    pisitools.dosed("Makefile", "Class\-Path\: \$\(JARDIR\)\/hexdump.jar", "Class-Path: hexdump.jar")
    autotools.make("-j1")

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("changelog", "COPYING", "README")

