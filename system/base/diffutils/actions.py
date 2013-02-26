#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #who knows pisitools.dosed :)
    cmd="sed -i '/gets is a security hole/d' lib/stdio.in.h"
    shelltools.system(cmd)
    # shelltools.touch("man/*.1")
    # shelltools.chmod("config/*", 0775)

    # disable automagic libsigsegv dependency
    shelltools.export("AUTOPOINT", "true")
    shelltools.export("ac_cv_libsigsegv", "no")

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-nls")

def build():
    autotools.make('LDFLAGS="%s"' % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "NEWS", "README")

