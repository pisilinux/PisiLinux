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

def setup():
    pisitools.dosed("Makefile", "\/usr\/local", "/usr")

def build():
    autotools.make("-j1 bin")

def install():
    autotools.make("DESTDIR=%s install-bin" % get.installDIR())

    pisitools.dodoc("AUTHORS", "changelog", "COPYING", "INSTALL", "README")

