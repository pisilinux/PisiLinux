#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fiv")
    autotools.configure("--with-python \
                         --with-cairo")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/oaf")
    # Conflicts with inscape, anyway, this file shouldn't be placed
    # in the package.
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
