#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()
    pisitools.dosed("Makefile.config", "MANDIR=.*", "MANDIR=/usr/share/man")
    pisitools.dosed("Makefile", "DESTDIR\)\$\(SHAREDIR\)/python/", "DESTDIR)$(LIBDIR)/%s/site-packages/" % get.curPYTHON())

def build():
    autotools.make("-j1 all.opt")

"""
def check():
    shelltools.export("LD_LIBRARY_PATH", get.curDIR())
    shelltools.system("./spatch.opt -sp_file demos/simple.cocci demos/simple.c")
"""

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/spatch")
    pisitools.domove("/usr/bin/spatch.opt", "/usr/bin", "spatch")

    shelltools.system("strip %s/usr/share/coccinelle/spatch.opt" % get.installDIR())

    for doc in shelltools.ls("*.txt"):
        pisitools.dodoc(doc)
