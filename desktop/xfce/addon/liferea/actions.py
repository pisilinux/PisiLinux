#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-sm \
                        --disable-schemas-install \
                        --enable-nm \
                        --enable-dbus \
                        --enable-libnotify")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    # Empty files: NEWS
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
