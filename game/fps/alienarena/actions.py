#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("PTHREAD_LIBS", "-lpthread")
shelltools.export("PTHREAD_CFLAGS", "-pthread")

def setup():
    # Use system libopenal
    pisitools.dosed("source/unix/qal_unix.c", "libopenal.so", "$LIBOPENAL")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.rename("/usr/bin/crx", "alienarena")
    #pisitools.rename("/usr/bin/crx-ded", "alienarena-server")

