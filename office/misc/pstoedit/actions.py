#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "-pedantic ", "")
    pisitools.dosed("configure.ac", "CXXFLAGS=\"-g\"", "")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --with-emf \
                         --with-swf")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/pstoedit.1")
    pisitools.dohtml("doc/*.htm")

    pisitools.dodoc("doc/readme.txt")
