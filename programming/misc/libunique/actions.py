#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export('HOME', get.workDIR())
def setup():
    autotools.configure("--disable-static \
                         --enable-gtk-doc \
                         --enable-maintainer-flags=no \
                         --enable-introspection=yes")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
