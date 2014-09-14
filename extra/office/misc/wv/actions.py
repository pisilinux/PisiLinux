#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-libwmf \
                         --disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/include", "wvinternal.h")
    pisitools.dosym("/usr/share/man/man1/wvWare.1", "/usr/share/man/man1/wvConvert.1")

    pisitools.dodoc("COPYING", "README")
