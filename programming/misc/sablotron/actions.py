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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "Sablot-%s" % get.srcVERSION()

def setup():
    for f in ["AUTHORS", "ChangeLog", "NEWS"]:
        shelltools.touch(f)

    autotools.autoreconf("-fi")
    libtools.libtoolize()

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/doc/%s" % get.srcNAME())
    pisitools.domove("/usr/share/doc/html", "/usr/share/doc/%s" % get.srcNAME())
    pisitools.dodoc("README*")
