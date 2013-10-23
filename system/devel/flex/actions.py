#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-fPIC")
    shelltools.export("AUTOPOINT", "true")

    autotools.autoreconf("-vfi")
    # do not enable nls http://bugs.gentoo.org/121408
    autotools.configure("--disable-nls \
                         --disable-dependency-tracking")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("flex", "/usr/bin/lex")

    pisitools.dodoc("NEWS", "README")
