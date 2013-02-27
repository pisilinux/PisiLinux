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
    shelltools.move("Makefile.def", "Makefile")
    autotools.make("-f Makefile CFLAGS='%s -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE'" % get.CFLAGS())

def install():
    pisitools.dobin("compress")
    pisitools.dosym("compress", "/usr/bin/uncompress")

    pisitools.doman("compress.1")
    pisitools.dosym("compress.1", "/usr/share/man/man1/uncompress.1")
