#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="./Digest-MD5-2.52"

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# FIXME: test fails
def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    
    pisitools.remove("/usr/share/man/man3/Digest::MD5.3pm")