#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "db-%s/build_unix" % get.srcVERSION()

shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")

def setup():
    shelltools.system("../dist/configure \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --datadir=/usr/share \
                       --sysconfdir=/etc \
                       --localstatedir=/var/lib \
                       --libdir=/usr/lib \
                       --enable-compat185 \
                       --with-uniquename \
                       --enable-java \
                       --disable-cxx \
                       --disable-tcl \
                       --disable-static")

def build():
    autotools.make()

def install():
    pisitools.dolib(".libs/libdb_java*.so")
    pisitools.insinto("/usr/share/java","db.jar")
