#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options = "--disable-static \
               --enable-noexecstack"

    if get.buildTYPE() == "emul32":
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

        # Use 32-bit assembler, another option is to use --disable-asm option
        pisitools.dosed("mpi/config.links", "path=\"amd64\"", "path=\"i586 i386\"")

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32": return

    pisitools.dodir("/etc/gcrypt")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "THANKS", "TODO")
