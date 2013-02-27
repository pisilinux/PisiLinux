#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("BASH=/bin/bash")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "FAQ", "README", "AUTHORS", "doc/*")
