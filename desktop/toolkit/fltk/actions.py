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
    pisitools.flags.add("-fPIC")
    pisitools.dosed("makeinclude.in", "^(docdir.*)$", r"\1/html")

    autotools.autoconf()
    autotools.configure("--enable-gl \
                         --enable-shared \
                         --enable-threads \
                         --with-optim='%s' \
                         " % get.CFLAGS())

def build():
    autotools.make()
    autotools.make("-C documentation all")

def install():
    autotools.install()
    autotools.install("-C documentation")
    autotools.rawInstall("DESTDIR=%s -C fluid" % get.installDIR(), "install-linux")

    pisitools.dodoc("ANNOUNCEMENT", "CHANGES", "COPYING", "CREDITS", "README")
