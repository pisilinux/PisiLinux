#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "GDGraph-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()
    autotools.make("samples")

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("CHANGES", "README")
