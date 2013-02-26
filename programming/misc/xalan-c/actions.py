#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="xml-xalan/c"

def setupVars():
    shelltools.export("XERCESCROOT","/usr/include/xercesc")
    shelltools.export("XALANCROOT","%s" % get.curDIR())
    shelltools.export("ICUROOT","/usr")
    shelltools.export("XALAN_USE_ICU","true")

def setup():
    setupVars()

    pisitools.dosed("runConfigure", '^CXXFLAGS="\\$compileroptions', "CXXFLAGS=\"${CXXFLAGS}")
    pisitools.dosed("runConfigure", '^CFLAGS="\\$compileroptions', "CFLAGS=\"${CXXFLAGS}")

    shelltools.system("./runConfigure -p linux -c gcc -x g++ -P /usr -t icu -C --libdir=/usr/lib")

def build():
    setupVars()
    autotools.make("-j1")

def install():
    setupVars()
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    # This comes from ICU
    pisitools.remove("/usr/lib/libicui18n.*")
