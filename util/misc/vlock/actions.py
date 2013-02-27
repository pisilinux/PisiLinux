#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --bindir=/usr/bin \
                            --sbindir=/usr/sbin \
                            --libdir=/usr/lib \
                            --mandir=/usr/share/man")

def build():
    autotools.make('CC=%s CFLAGS="%s -std=gnu99"' % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING", "PLUGINS", "README*", "SECURITY", "STYLE", "TODO")

