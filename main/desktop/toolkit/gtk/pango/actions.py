#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    if get.buildTYPE()=="emul32":
        pisitools.dosed("pango/modules.c", "(pango\.modules)", r"\1-32")
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --sysconfdir=/etc \
                         --with-included-modules=basic-fc \
                         --%sable-introspection" % ("dis" if get.buildTYPE()=="emul32" else "en"))

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE()=="emul32":
        shelltools.move("pango/.libs/pango-querymodules", "pango/.libs/pango-querymodules-32")
        pisitools.dobin("pango/.libs/pango-querymodules-32")
        return

    pisitools.dodir("/etc/pango")
    shelltools.touch(get.installDIR() +"/etc/pango/pango.modules")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "README", "NEWS")
