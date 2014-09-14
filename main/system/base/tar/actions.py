#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-vfi")

    # For being able to build as root, pff
    shelltools.export("FORCE_UNSAFE_CONFIGURE", "1")
    autotools.configure("--bindir=/bin \
                         --libexecdir=/bin \
                         --disable-rpath \
                         --enable-nls")

def build():
    autotools.make()

# test has a sandbox problem disabled.
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.doman("doc/tar.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "THANKS")

