#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft PiSi GNU/Linux Community
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

suffix = "32" if get.buildTYPE() == "emul32" else ""

def setup():
    autotools.rawConfigure("--libdir=/lib%s \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib%s \
                            --bindir=/bin%s" % ((suffix,)*3))
def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install install-lib install-dev" % get.installDIR())
    if get.buildTYPE() == "emul32": pisitools.removeDir("/bin32")
    pisitools.remove("/lib%s/*.a" % suffix)
