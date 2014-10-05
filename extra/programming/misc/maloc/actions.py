#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


def setup():
	autotools.autoreconf("-vif")
	autotools.autoconf()
	libtools.libtoolize("--copy --force")
	libtools.libtoolize("--automake")
	autotools.aclocal("-I m4")
	autotools.autoheader()
	autotools.configure("--disable-static \
						 --docdir=/usr/share/doc/maloc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/*txt")