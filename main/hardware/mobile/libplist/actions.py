#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    #  do not link with installed old library
    pisitools.dosed("cython/Makefile.*", "(plist_la_LDFLAGS\s=.*)(\s-L\$\(libdir\))(.*)", r"\1\3")

    autotools.configure("\
                         --disable-static \
                         --disable-silent-rules \
                        ")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LESSER", "README")
