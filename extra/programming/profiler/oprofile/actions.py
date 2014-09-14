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
    for i in ["AUTHORS", "NEWS", "ChangeLog"]:
        shelltools.touch(i)

    autotools.autoreconf("-fi")
    autotools.configure("--enable-static=no \
                         --with-x \
                         --enable-gui=qt4")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "TODO", "AUTHORS", "COPYING", "ChangeLog*")
