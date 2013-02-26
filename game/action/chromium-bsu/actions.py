#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure('--with-font-path="/usr/share/fonts/dejavu/DejaVuSerif-Bold.ttf"')

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "NEWS", "README", "AUTHORS", "ChangeLog")
