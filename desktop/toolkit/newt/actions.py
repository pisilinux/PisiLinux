#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.echo("config.h.in", "#define USE_INTERP_RESULT 1")
    autotools.configure("--prefix=/usr \
                         --with-gpm-support")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove static lib
    pisitools.remove("/usr/lib/libnewt.a")

    pisitools.dodoc("CHANGES", "COPYING")

