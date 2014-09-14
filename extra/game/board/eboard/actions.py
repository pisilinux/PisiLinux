#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import libtools

def setup():
    libtools.libtoolize("--copy --force")

    autotools.configure("--man-prefix=/usr/share/man --extra-libs=dl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "icon-eboard.xpm")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO")
