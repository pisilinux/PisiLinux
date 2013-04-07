#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    pisitools.dosed("configure.ac", "DG_DISABLE_DEPRECATED", deleteLine = True)
    autotools.autoreconf("-fiv")
    autotools.configure("--enable-manpages \
                         --disable-strict \
                         --disable-coverage \
                         --enable-gcrypt \
                         --enable-introspection \
                         --disable-vala \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

