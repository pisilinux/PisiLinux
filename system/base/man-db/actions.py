#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
     autotools.configure("--disable-setuid \
                          --disable-rpath \
                          --with-sections=\"1 1p 8 2 3 3p 4 5 6 7 9 0p n l p o 1x 2x 3x 4x 5x 6x 7x 8x\" \
                          --docdir=/%s/%s \
                          --with-device=utf8 \
                          --enable-mb-groff" % (get.docDIR(), get.srcNAME()))

def build():
    shelltools.system("sed -i '/gets is a security hole/d' gnulib/lib/stdio.in.h")  
    autotools.make("CC='%s %s' V=1 nls=all" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/cache/man")

    # These are shipped with groff
    pisitools.remove("/usr/bin/zsoelim")
    pisitools.remove("/usr/share/man/man1/zsoelim.1")

    pisitools.dodoc("README")
