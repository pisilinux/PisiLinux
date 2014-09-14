#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "LGPL", "blob-examples/SAMSUNG*",
                    "blob-examples/ST*", "blob-examples/Maxtor*",
                    "blob-examples/WDC*", "blob-examples/FUJITSU*",
                    "blob-examples/INTEL*", "blob-examples/TOSHIBA*",
                    "blob-examples/MCC*")

