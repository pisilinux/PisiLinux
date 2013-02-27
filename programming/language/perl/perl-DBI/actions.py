#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    shelltools.export("LC_ALL", "C")
    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("README", "Changes")
