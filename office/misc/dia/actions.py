#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--with-python \
                         --with-cairo \
                         --enable-libemf")

def build():
    autotools.make()

def install():
    autotools.install()

    #pisitools.removeDir("/usr/share/oaf")
    # Conflicts with inscape, anyway, this file shouldn't be placed
    # in the package.
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")