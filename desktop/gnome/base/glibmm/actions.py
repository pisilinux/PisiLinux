#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    dirs = ["/usr/share/doc", "/usr/share/devhelp"]
    for dir in dirs:
        pisitools.removeDir(dir)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
