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

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")
    autotools.rawInstall("DESTDIR=%s INSTALL_DIR=/usr/bin MAN_DIR=/usr/share/man/man1" % get.installDIR())

    pisitools.dodoc("BUGS", "CHANGES", "README", "TODO")
