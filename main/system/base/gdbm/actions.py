#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-libgdbm-compat")

def build():
    autotools.make("prefix=/usr")

def install():
    autotools.install("prefix=%s/usr" % get.installDIR())

    pisitools.dosym("../gdbm.h", "/usr/include/gdbm/gdbm.h")
    pisitools.dosym("../dbm.h", "/usr/include/gdbm/dbm.h")
    pisitools.dosym("../nbm.h", "/usr/include/gdbm/ndbm.h")

    pisitools.dodoc("ChangeLog", "NEWS", "README")
