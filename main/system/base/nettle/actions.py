#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    options = "--enable-shared"

    if not get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        #pisitools.remove("/usr/lib32/*.a")
        return

    #pisitools.remove("/usr/lib/*.a")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README", "nettle.pdf")
