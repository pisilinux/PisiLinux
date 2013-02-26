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

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--enable-static=no")

def build():
    autotools.make("-j1")

def install():
    pisitools.doexe("src/.libs/pam_p11_opensc.so", "/lib/security")
    pisitools.doexe("src/.libs/pam_p11_openssh.so", "/lib/security")

    pisitools.dodoc("doc/ChangeLog", "COPYING", "NEWS")
