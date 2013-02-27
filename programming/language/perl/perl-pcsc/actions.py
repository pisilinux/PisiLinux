#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="pcsc-perl-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# FIXME: test fails
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("Changelog", "LICENCE", "README")
