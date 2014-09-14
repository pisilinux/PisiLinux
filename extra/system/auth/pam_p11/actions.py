#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

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
