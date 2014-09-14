#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-std-include")

    flagorderrx = (r"(\\\$deplibs \\\$postdep_objects) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *flagorderrx)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CREDITS", "LICENSE", "NOTICE", "README")
