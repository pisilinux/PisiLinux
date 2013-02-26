#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dohtml("httrack-doc.html")

    pisitools.dodoc("AUTHORS", "README", "greetings.txt", "history.txt")
