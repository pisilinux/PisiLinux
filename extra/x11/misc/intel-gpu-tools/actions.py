#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools


shelltools.system("export LC_ALL=C")
shelltools.export("LANG", "en_US.UTF-8")

def setup():
    autotools.configure("--disable-tests \
                         --disable-dumper")

def build():
    autotools.make()

def install():
    autotools.install()
