#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-shared \
                         --disable-static")
def build():
    autotools.make()

#def check():
    #autotools.make("check")

def install():
    autotools.install()

    autotools.make("distclean")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcNAME(), "examples")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
