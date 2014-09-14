#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/Makefile.in", "dvips", "#dvips")
    pisitools.dosed("xglyph/xglyph.c", "\./\(t1lib\.config\)", "/etc/t1lib/\1")

    autotools.configure("--datadir=/etc \
                         --with-x \
                         --enable-static=no")


def build():
    autotools.make("without_doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("Changes", "README*")
