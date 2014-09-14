#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DUSE_INTERP_RESULT" % get.CFLAGS())

    autotools.configure('--with-tk="/usr/lib" \
                         --with-tcl="/usr/lib" \
                         --enable-devlibs')

def build():
    autotools.make("PREFIX=/usr MANDIR=/usr/share/man")
    autotools.make("hfsck/hfsck")

def install():
    for d in ["/usr/bin", "/usr/share/man/man1", "/usr/lib", \
                "/usr/include"]:
        pisitools.dodir(d)

    pisitools.dobin("hfsck/hfsck")
    # Create fsck.hfs
    pisitools.dosym("hfsck", "/usr/bin/fsck.hfs")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("BLURB", "CHANGES", "COPYING", "COPYRIGHT", "CREDITS", \
                    "README*", "TODO")
