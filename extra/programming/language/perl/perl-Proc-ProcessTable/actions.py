#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

# Package stalls while testing, just skip this part.
#def check():
    #perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("Changes", "PORTING", "README", "README.linux", "TODO", "example.pl", "contrib/pswait")

