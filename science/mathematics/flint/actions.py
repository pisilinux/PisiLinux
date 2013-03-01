#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('FLINT_TUNE="%s" \
                    FLINT_GMP_LIB_DIR=/usr/lib \
                    FLINT_LINK_OPTIONS="%s" \
                    FLINT_CC=%s \
                    MAKECMDGOALS=library libflint.a libflint.so' % (get.CFLAGS(), get.LDFLAGS(), get.CC()))

def install():
    pisitools.dolib_so("libflint.so.0")
    pisitools.dosym("libflint.so.0", "/usr/lib/libflint.so")

    pisitools.dolib_a("libflint.a")

    for header in [h for h in shelltools.ls(".") if h.endswith(".h")]:
        pisitools.insinto("/usr/include/flint", header)

    pisitools.dodoc("doc/*.pdf")
    pisitools.dodoc("CHANGES.txt","gpl-2.0.txt","todo.txt")
