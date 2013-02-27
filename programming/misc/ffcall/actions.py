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
                         --enable-shared")

def build():
    autotools.make("-j1")

def install():
    pisitools.dodir("/usr/share")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/html/", "/usr/share/doc/%s/" % get.srcNAME())

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("COPYING", "NEWS", "README")
