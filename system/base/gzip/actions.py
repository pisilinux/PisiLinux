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
    #shelltools.export("DEFS", "NO_ASM")
    autotools.configure("--exec-prefix=/")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add missing gzcat
    pisitools.dosym("zcat", "/bin/gzcat")

    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")
