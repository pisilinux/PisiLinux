#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def setup():
    autotools.configure("--enable-shared")

    shelltools.chmod("examples/*", 0644)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "THANKS", "doc/LZO*")

    pisitools.insinto(examples, "examples/*.c")
    pisitools.insinto(examples, "examples/*.h")
