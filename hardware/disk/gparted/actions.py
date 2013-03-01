#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    # Don't call gtk
    pisitools.dosed("data/icons/Makefile.in", "^install-data-local: .*$", "install-data-local: install-icons")
    autotools.configure("--disable-doc")

def build():
    autotools.make()

def install():
    autotools.install()
