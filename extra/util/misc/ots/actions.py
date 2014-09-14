#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.touch("gtk-doc.make")
    shelltools.system('sed -i -e "s/en.xml$//" dic/Makefile.am')

    autotools.autoreconf("-vif")
    libtools.libtoolize("--force")

    autotools.configure('--prefix=/usr \
                         --disable-static')

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "HACKING", "README*",
                    "NEWS", "TODO")
