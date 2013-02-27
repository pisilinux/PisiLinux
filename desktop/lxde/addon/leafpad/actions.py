#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-dependency-tracking \
                         --enable-chooser \
                         --enable-print")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

