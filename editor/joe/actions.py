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
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "HINTS", "LIST", "NEWS", "README", "TODO")

    # Default joe man includes informations for below applications
    for app in ["jmacs", "jpico", "jstar", "rjoe"]:
        pisitools.dosym("/usr/share/man/man1/joe.1", "/usr/share/man/man1/%s.1" % app)

