#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SVK-v%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# Disable tests temporarily
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()
