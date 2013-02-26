#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    #prevent sandbox violation
    pisitools.dosed("autowaf.py", "/sbin/ldconfig", "/bin/true")

    #remove unnecessary flags
    pisitools.dosed("slv2.pc.in", "@REDLAND.*@", "")

    shelltools.system("python waf configure --prefix=/usr --libdir=/usr/lib/")

def build():
    shelltools.system("python waf build -v")

def install():
    shelltools.system("DESTDIR=%s ./waf install" % get.installDIR())
    shelltools.chmod("%s/usr/lib/lib*.so*" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
