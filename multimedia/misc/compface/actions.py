#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

sd = "shared"

def setup():
    shelltools.makedirs(sd)
    shelltools.cd(sd)
    shelltools.sym("libcompface.so", "libcompface.so.1")
    shelltools.sym("libcompface.so.1.0.0", "libcompface.so")

def build():
    shelltools.cd(sd)
    autotools.make('-f ../Makefile \
                    VPATH=".." \
                    srcdir=".." \
                    LDFLAGS="-lc" \
                    CFLAGS="%s -L%s -fPIC -pipe -D_BSD_SOURCE -D_REENTRANT" \
                    shared' % (get.CFLAGS(), sd))

    shelltools.cd("..")
    autotools.make()

def install():
    pisitools.dolib_so("%s/libcompface.so.1.0.0" % sd)
    pisitools.dosym("libcompface.so.1.0.0", "/usr/lib/libcompface.so.1")
    pisitools.dosym("libcompface.so.1", "/usr/lib/libcompface.so")

    pisitools.insinto("/usr/include", "compface.h")

    for f in ["xbm2xface.pl", "compface", "uncompface"]:
        pisitools.dobin(f)

    for f in ["compface.1", "compface.3"]:
        pisitools.doman(f)

    pisitools.dodoc("ChangeLog", "README")

