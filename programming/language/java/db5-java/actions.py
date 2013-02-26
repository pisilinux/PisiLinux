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

import os

WorkDir = "db-%s/build_unix" % get.srcVERSION()

def setup():
    shelltools.export("PATH", "%s:/opt/sun-jdk/bin" % os.environ.get("PATH"))

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
    shelltools.export("PATH", "%s:/opt/sun-jdk/bin" % os.environ.get("PATH"))
    autotools.make()

def install():
    pisitools.dolib(".libs/libdb_java*.so")
    pisitools.insinto("/usr/share/java","db.jar")
