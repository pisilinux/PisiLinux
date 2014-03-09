#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --disable-silent-rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# solve conflict with elfutils and glibc-devel
#    pisitools.remove("/usr/include/nlist.h")
#    pisitools.remove("/usr/lib/libbsd.a")

    pisitools.dodoc("ChangeLog", "COPYING", "README", "TODO")
