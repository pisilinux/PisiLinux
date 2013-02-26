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

shelltools.export("HOME", get.workDIR())

def setup():
    #shelltools.system("./autogen.sh")

    autotools.configure("--enable-mime \
                         --enable-extras \
                         --enable-contrast")

    pisitools.dosed("Makefile", "/usr/lib/gimp/", "%s/usr/lib/gimp/" % get.installDIR())

def build():
    autotools.make("schemasdir=/etc/gconf/schemas")

def install():
    autotools.install("schemasdir=%s/etc/gconf/schemas" % get.installDIR())

    # Do not conflict with dcraw package
    pisitools.remove("/usr/bin/dcraw")

    pisitools.insinto("/usr/share/mime/packages", "ufraw-mime.xml")

    pisitools.dodoc("COPYING", "MANIFEST", "README")
