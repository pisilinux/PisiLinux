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

def setup():
    autotools.configure("--disable-static \
                         --enable-python \
                         --enable-php ")

def build():
    autotools.make()
    autotools.make("check")

    shelltools.cd("doc")
    autotools.make("doxygen-html")

def install():
    autotools.rawInstall("DESTDIR=%(D)s \
                          PYTHON_PREFIX=%(D)s/usr/lib/%(V)s \
                          PYTHON_EXEC_PREFIX=%(D)s/usr/lib/%(V)s" % {"D": get.installDIR(),
                                                                     "V": get.curPYTHON()})

    pisitools.insinto("/usr/share/doc/geos", "doc/doxygen_docs/html")
    pisitools.dodoc("README", "ChangeLog", "AUTHORS", "NEWS", "COPYING")
