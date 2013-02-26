#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "astyle"

def build():
    pisitools.dosed("build/intel/Makefile","/share/astyle","/share/doc/astyle/html")
    pisitools.dosed("build/gcc/Makefile","/share/astyle","/share/doc/astyle/html")
    shelltools.cd("build/gcc")
    autotools.make("release shared")

def install():
    shelltools.cd("build/gcc")
    autotools.install()
    shelltools.cd("%s/%s" % (get.workDIR() , WorkDir))
    pisitools.dohtml("doc/*") 