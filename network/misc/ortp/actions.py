#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-shared \
                         --disable-strict \
                         --disable-static")

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *replace)

def build():
    autotools.make()

def install():
    autotools.install("pkgdocdir=%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("README", "ChangeLog", "NEWS", "COPYING", "AUTHORS", "TODO")
