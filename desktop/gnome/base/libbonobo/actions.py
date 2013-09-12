#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("activation-server/", "DG_DISABLE_DEPRECATED", filePattern = "Makefile\.(am|in)", deleteLine = True)
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --enable-bonobo-activation-debug=no")
    pisitools.dosed("libtool"," -shared "," -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "NEWS", "README", "ChangeLog", "AUTHORS")
