#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# Disable tests as perl-Sane tests tries to reach files under /dev
#def check():
#    perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "examples")
    pisitools.dodoc("Changes", "README")

