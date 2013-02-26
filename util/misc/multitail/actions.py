#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make("all")

def install():
    pisitools.dobin("multitail")

    pisitools.dosed('multitail.conf', 'check_mail:5', 'check_mail:0')  # disable check mail feature by default
    pisitools.insinto("/etc", "multitail.conf")

    pisitools.dodoc("Changes", "license.txt", "readme.txt")
    pisitools.dohtml("manual*.html")
    pisitools.doman("multitail.1")
