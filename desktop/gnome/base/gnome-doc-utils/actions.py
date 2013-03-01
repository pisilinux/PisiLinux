#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.copy("tools/gnome-doc-utils.m4", "m4/")
    autotools.autoreconf("-fiv")
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")
