#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir="snack%s/unix" % get.srcVERSION()

def setup():
    shelltools.cd("unix")
    autotools.rawConfigure("--with-tcl=/usr/lib \
                            --with-tk=/usr/lib \
                            --enable-alsa \
                            --enable-threads \
                            --with-ogg-include=/usr/include \
                            --with-ogg-lib=/usr/lib")

def build():
    shelltools.cd("unix")
    pisitools.dosed("Makefile", "^CFLAGS    = -O", "CFLAGS    =  %s" %get.CFLAGS())
    autotools.make()

def install():
    shelltools.cd("unix")
    pisitools.insinto("/usr/lib/snack","*.so")
    pisitools.insinto("/usr/lib/snack","*.tcl")

    pisitools.dodoc("../doc/*.txt")
    pisitools.dohtml("../doc/*.html")
