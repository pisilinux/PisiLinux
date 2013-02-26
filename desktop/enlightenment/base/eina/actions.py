#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fvisibility=hidden" % get.CFLAGS())
shelltools.export("LDFLAGS", "%s -fvisibility=hidden" % get.LDFLAGS())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-amalgamation \
                         --enable-valgrind \
                         --with-internal-maximum-log-level=3 \
                         --disable-static \
                         --disable-benchmark \
                         --disable-install-examples \
                         --disable-build-examples \
                         --disable-doc \
                         --disable-tests \
                         --enable-default-mempool \
                         --enable-mempool-chained-pool \
                         --enable-mempool-pass-through \
                         --disable-mempool-buddy \
                         --disable-mempool-ememoa-fixed \
                         --disable-mempool-ememoa-unknown \
                         --disable-mempool-fixed-bitmap \
                         --disable-assert \
                         --disable-ememoa \
                         --enable-magic-debug \
                         --enable-safety-checks")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.removeDir("/usr/bin")
    #pisitools.removeDir("/usr/share")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
