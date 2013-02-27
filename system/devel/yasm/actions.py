#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


flags = "%s -fPIC" % get.CFLAGS() if get.ARCH() == "x86_64" else get.CFLAGS()

def setup():
    shelltools.export("CFLAGS", flags)

    autotools.configure("--enable-nls \
                         --disable-rpath")
                         # --enable-python \
                         # --enable-python-bindings \

def build():
    autotools.make()

# FIXME: python tests fail, others fail in 64bit, gentoo says tests are wrong
def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "BSD.txt", "GNU_GPL-2.0", "GNU_LGPL-2.0", "Artistic.txt")

