#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-test-themes \
                         --enable-icon-mapping")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

    pisitools.remove("/usr/share/themes/*/index.theme")
    pisitools.remove("/usr/share/icons/*/index.theme")
