#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "doc/README.bin")

    pisitools.domove("/usr/share/sphinx2/doc/*", "/usr/share/doc/sphinx2/")
    pisitools.removeDir("/usr/share/sphinx2/doc")
