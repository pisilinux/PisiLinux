#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    options = "--enable-shared \
               --disable-dependency-tracking"
               
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

    shelltools.chmod("examples/*", 0644)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "doc/LZO*")

    pisitools.insinto(examples, "examples/*.c")
    pisitools.insinto(examples, "examples/*.h")
