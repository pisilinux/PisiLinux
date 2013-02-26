#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-snapshot-%s" % (get.srcNAME(), get.srcVERSION())

def setup():
    autotools.configure("--disable-static \
                         --disable-debug \
                         --with-gcrypt ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/ggz.modules.d")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
