#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("\
                         --without-libsigsegv \
                         --enable-switch \
                         --enable-nls \
                        ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove versioned binaries
    pisitools.remove("/usr/bin/*-*")

    pisitools.dosym("gawk.1", "/usr/share/man/man1/awk.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
