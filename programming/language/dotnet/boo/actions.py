#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("MONO_SHARED_DIR", ".")

def setup():
    pisitools.dosed("extras/boo.pc.in", "/lib", "/lib/mono")
    autotools.rawConfigure("--prefix=/usr \
                            --libdir=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove unused directory
    pisitools.removeDir("/share")

    # Empty files: NEWS, README, ChangeLog
    pisitools.dodoc("AUTHORS", "COPYING")
