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

def setup():
    autotools.configure("--enable-nls \
                         --program-prefix=g")

def build():
    autotools.make()

def check():
    shelltools.export("LANG", "C")
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("gmake", "/usr/bin/make")
    pisitools.dosym("gmake.1","/usr/share/man/man1/make.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*")
