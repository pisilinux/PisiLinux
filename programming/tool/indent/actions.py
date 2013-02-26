#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.touch("man/Makefile.am")
    shelltools.touch("man/texinfo2man.c")

    autotools.configure("--enable-nls")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("%s/usr/doc/indent/" % get.installDIR())
    pisitools.removeDir("/usr/doc")
    pisitools.dodoc("AUTHORS", "NEWS", "README*")
