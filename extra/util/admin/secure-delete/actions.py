#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "secure_delete-%s" % get.srcVERSION()

def build():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.make()

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())

    pisitools.doman("*.1")
    pisitools.dodoc("CHANGES", "FILES", "README*", "TODO", "*.doc")

    pisitools.rename("/usr/bin/smem", "sdmem")
    pisitools.rename("/usr/share/man/man1/smem.1", "sdmem.1")

